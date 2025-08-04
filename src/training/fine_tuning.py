"""
Fine-tuning script using HuggingFace Transformers Trainer.
Loads pre-trained models, fine-tunes on custom dataset, and saves artifacts to S3.
"""
import boto3
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

s3_client = boto3.client('s3')

def upload_to_s3(local_path: str, bucket_name: str, s3_key: str):
    s3_client.upload_file(local_path, bucket_name, s3_key)

def main():
    dataset = load_dataset("imdb")
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        per_device_train_batch_size=8,
        per_device_eval_batch_size=8,
        num_train_epochs=1,
        weight_decay=0.01
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset["train"].shuffle(seed=42).select(range(1000)),
        eval_dataset=tokenized_dataset["test"].shuffle(seed=42).select(range(500))
    )
    trainer.train()

    model.save_pretrained("./model")
    tokenizer.save_pretrained("./model")

    upload_to_s3("./model/config.json", "my-mlops-bucket", "model/config.json")
    upload_to_s3("./model/pytorch_model.bin", "my-mlops-bucket", "model/pytorch_model.bin")

if __name__ == "__main__":
    main()

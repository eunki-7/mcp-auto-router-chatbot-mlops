install:
	pip install -r requirements.txt

run:
	uvicorn src.inference.main:app --host 0.0.0.0 --port 8000 --reload

test:
	pytest tests/

docker-build:
	docker build -t chatbot:latest .

docker-run:
	docker run -p 8000:8000 chatbot:latest

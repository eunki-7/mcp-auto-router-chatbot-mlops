#!/bin/bash
# Script to build and push Docker image to ECR
REPO_NAME=$1
AWS_REGION=$2
if [ -z "$REPO_NAME" ] || [ -z "$AWS_REGION" ]; then
    echo "Usage: ./ecr_push.sh <repo-name> <aws-region>"
    exit 1
fi
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
ECR_URI="${ACCOUNT_ID}.dkr.ecr.${AWS_REGION}.amazonaws.com/${REPO_NAME}"
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ECR_URI
docker build -t ${REPO_NAME}:latest .
docker tag ${REPO_NAME}:latest ${ECR_URI}:latest
docker push ${ECR_URI}:latest
echo "Image pushed to ${ECR_URI}:latest"

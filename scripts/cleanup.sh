#!/bin/bash
# Stop and remove all Docker containers and volumes related to this project
echo "Stopping running containers..."
docker ps -q --filter "ancestor=chatbot:latest" | xargs -r docker stop

echo "Removing stopped containers..."
docker ps -a -q --filter "ancestor=chatbot:latest" | xargs -r docker rm

echo "Removing dangling images and volumes..."
docker image prune -f
docker volume prune -f

echo "Cleanup completed."

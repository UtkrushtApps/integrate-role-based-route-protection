#!/bin/bash
set -e

echo "[install.sh] Starting installation/setup..."

if ! command -v docker &> /dev/null; then
    echo "[install.sh] Docker could not be found. Please install Docker."
    exit 1
fi

echo "[install.sh] Building Docker image..."
docker build -t fastapi-ecommerce .

echo "[install.sh] Creating/Starting Docker container..."
docker rm -f fastapi-ecommerce-container 2>/dev/null || true

docker run -d --name fastapi-ecommerce-container -p 8000:8000 --env-file .env fastapi-ecommerce

echo "[install.sh] Installation complete. App should be running in the container."

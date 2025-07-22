#!/bin/bash
set -e

./install.sh

echo "[run.sh] Checking container logs..."
docker logs fastapi-ecommerce-container --tail 20

echo "[run.sh] App should be available at http://localhost:8000"

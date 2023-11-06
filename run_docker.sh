#!/bin/bash

# Run the FastAPI app container, mapping port 8000 on the host to port 8000 in the container
docker run -p 8000:8000 fastapi-app

docker pull your-dockerhub-username/fastapi-app:latest
docker run -d -p 8000:80 your-dockerhub-username/fastapi-app:latest

#!/bin/bash

NAMESPACE="rabbitmq-application"
DEPLOYMENT_NAME="node-publisher-api"
IMAGE_NAME="registry.lambda-it.ch/library/hackweek-kevin/$DEPLOYMENT_NAME:latest"

echo "Build Docker Image"
docker build -t $IMAGE_NAME .

docker push $IMAGE_NAME

echo "Restarting deployment $DEPLOYMENT_NAME"
kubectl rollout restart deployment "$DEPLOYMENT_NAME" -n "$NAMESPACE"

echo "Deployment complete."
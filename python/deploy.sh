#!/bin/bash

NAMESPACE="rabbit-mq-applications"
DEPLOYMENT_NAME="python-queue-receiver-simple"
IMAGE_NAME="python-queue-receiver-simple:latest"

echo "Build Docker Image"
docker build -t $IMAGE_NAME .

# echo "Remove old Docker image from Minikube"
# minikube image rm $IMAGE_NAME
echo "Remove Deployment"
kubectl delete deployment python-queue-receiver-simple -n rabbit-mq-applications


echo "Load Docker Image into Minikube"
minikube image load $IMAGE_NAME

# Check if the namespace exists before attempting to create it
if kubectl get namespace "$NAMESPACE" >/dev/null 2>&1; then
    echo "Namespace $NAMESPACE already exists."
else
    echo "Creating namespace $NAMESPACE"
    kubectl create namespace "$NAMESPACE"
fi

echo "Apply application configuration"
kubectl apply -f deployment.yaml -n "$NAMESPACE"

# Restart the deployment to ensure the latest image is used
echo "Restarting deployment $DEPLOYMENT_NAME"
kubectl rollout restart deployment "$DEPLOYMENT_NAME" -n "$NAMESPACE"

echo "Deployment complete."

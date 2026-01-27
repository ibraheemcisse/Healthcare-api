#!/bin/bash
set -e

echo "🚀 Deploying Healthcare API to Kubernetes..."

# Get latest image SHA from Docker Hub
LATEST_SHA=$(git rev-parse HEAD)
IMAGE="ibraheemcisse/healthcare-api:${LATEST_SHA}"

echo "📦 Image: $IMAGE"

# Update deployment
kubectl set image deployment/healthcare-api \
  healthcare-api=$IMAGE

# Wait for rollout
echo "⏳ Waiting for rollout..."
kubectl rollout status deployment/healthcare-api

# Verify
echo "✅ Deployment complete!"
kubectl get pods -l app=healthcare-api

echo ""
echo "🎯 Healthcare API updated successfully!"

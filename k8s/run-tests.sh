#!/usr/bin/env bash
set -euo pipefail

CLUSTER_NAME="test-automation"
IMAGE_TAG="tests_automation:k8s"

echo "==> Building image"
docker build -t "$IMAGE_TAG" .

echo "==> Loading image into kind cluster '$CLUSTER_NAME'"
kind load docker-image "$IMAGE_TAG" --name "$CLUSTER_NAME"

echo "==> Removing previous test Jobs (if any)"
kubectl delete job tests-chromium tests-firefox --ignore-not-found

echo "==> Starting chromium and firefox test Jobs"
kubectl apply -f k8s/chromium-job.yaml -f k8s/firefox-job.yaml

echo "==> Waiting for Jobs to finish"
kubectl wait --for=condition=complete --timeout=120s job/tests-chromium job/tests-firefox 2>&1 || true

echo
echo "=== chromium results ==="
kubectl logs -l browser=chromium --tail=20

echo
echo "=== firefox results ==="
kubectl logs -l browser=firefox --tail=20

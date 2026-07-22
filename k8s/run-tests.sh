#!/usr/bin/env bash
set -euo pipefail

CLUSTER_NAME="test-automation"
IMAGE_TAG="tests_automation:k8s"

echo "==> Building image"
docker build -t "$IMAGE_TAG" .

echo "==> Loading image into kind cluster '$CLUSTER_NAME'"
kind load docker-image "$IMAGE_TAG" --name "$CLUSTER_NAME"

echo "==> Removing previous test Jobs (if any)"
kubectl delete job tests-chromium tests-firefox tests-api --ignore-not-found

echo "==> Starting chromium, firefox, and api test Jobs"
kubectl apply -f k8s/chromium-job.yaml -f k8s/firefox-job.yaml -f k8s/api-job.yaml

echo "==> Waiting for Jobs to finish"
kubectl wait --for=condition=complete --timeout=120s job/tests-chromium job/tests-firefox job/tests-api || true

echo
echo "=== chromium results ==="
kubectl logs -l browser=chromium --tail=20

echo
echo "=== firefox results ==="
kubectl logs -l browser=firefox --tail=20

echo
echo "=== api results ==="
kubectl logs -l suite=api --tail=20

echo
echo "==> Checking Job status"
CHROMIUM_SUCCEEDED=$(kubectl get job tests-chromium -o jsonpath='{.status.succeeded}')
FIREFOX_SUCCEEDED=$(kubectl get job tests-firefox -o jsonpath='{.status.succeeded}')
API_SUCCEEDED=$(kubectl get job tests-api -o jsonpath='{.status.succeeded}')

if [[ "$CHROMIUM_SUCCEEDED" != "1" || "$FIREFOX_SUCCEEDED" != "1" || "$API_SUCCEEDED" != "1" ]]; then
    echo "FAIL: one or more Jobs did not complete successfully" >&2
    exit 1
fi

echo "==> All Jobs completed successfully"

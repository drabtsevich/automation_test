#!/usr/bin/env bash
set -euo pipefail

CLUSTER_NAME="test-automation"
IMAGE_TAG="tests_automation:k8s"
IOS_APP_PATH="$PWD/apps/Payload/My Demo App.app"

# job name -> pod label selector
JOBS=(tests-chromium tests-firefox tests-api)
SELECTORS=(browser=chromium browser=firefox suite=api)

# --mobile also runs the iOS suite. It needs Appium and the simulator running on
# this Mac, so it's opt-in and the default run stays self-contained.
if [[ "${1:-}" == "--mobile" ]]; then
    if ! curl -sf http://127.0.0.1:4723/status >/dev/null; then
        echo "FAIL: Appium is not running on port 4723. Start it with:" >&2
        echo "  DEVELOPER_DIR=/Applications/Xcode.app/Contents/Developer appium" >&2
        exit 1
    fi
    if [[ ! -d "$IOS_APP_PATH" ]]; then
        echo "FAIL: iOS app not found at $IOS_APP_PATH" >&2
        exit 1
    fi
    JOBS+=(tests-mobile)
    SELECTORS+=(suite=mobile)
fi

echo "==> Building image"
docker build -t "$IMAGE_TAG" .

echo "==> Loading image into kind cluster '$CLUSTER_NAME'"
kind load docker-image "$IMAGE_TAG" --name "$CLUSTER_NAME"

echo "==> Removing previous test Jobs (if any)"
kubectl delete job tests-chromium tests-firefox tests-api tests-mobile --ignore-not-found

echo "==> Starting ${JOBS[*]} Jobs"
kubectl apply -f k8s/chromium-job.yaml -f k8s/firefox-job.yaml -f k8s/api-job.yaml
if [[ " ${JOBS[*]} " == *" tests-mobile "* ]]; then
    sed "s|__IOS_APP_PATH__|$IOS_APP_PATH|" k8s/mobile-job.yaml | kubectl apply -f -
fi

echo "==> Waiting for Jobs to finish"
# Poll until every Job is Complete or Failed; `kubectl wait --for=condition=complete`
# would block until the timeout on a Job that failed.
for _ in $(seq 1 90); do
    PENDING=0
    for job in "${JOBS[@]}"; do
        STATE=$(kubectl get job "$job" -o jsonpath='{.status.conditions[?(@.status=="True")].type}')
        [[ "$STATE" == *Complete* || "$STATE" == *Failed* ]] || PENDING=1
    done
    [[ "$PENDING" == "0" ]] && break
    sleep 2
done

for i in "${!JOBS[@]}"; do
    echo
    echo "=== ${JOBS[$i]#tests-} results ==="
    kubectl logs -l "${SELECTORS[$i]}" --tail=20
done

echo
echo "==> Checking Job status"
FAILED=0
for job in "${JOBS[@]}"; do
    if [[ "$(kubectl get job "$job" -o jsonpath='{.status.succeeded}')" != "1" ]]; then
        echo "FAIL: $job did not complete successfully" >&2
        FAILED=1
    fi
done
[[ "$FAILED" == "0" ]] || exit 1

echo "==> All Jobs completed successfully"

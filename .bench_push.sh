#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== PUSH ==="
git push net-kotobase HEAD:main 2>&1
echo "PUSH_RC=$?"
echo "=== POST-PUSH FETCH ==="
git fetch net-kotobase main 2>&1
echo "=== POST-PUSH HEAD ==="
git rev-parse HEAD
echo "=== POST-PUSH remote ==="
git rev-parse net-kotobase/main
} > /tmp/bench_push.txt 2>&1
echo PUSH_RAN
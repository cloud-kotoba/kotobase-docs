#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== push ==="
git push bench_fetch HEAD:main 2>&1
echo "rc=$?"
echo "=== post-push fetch ==="
git fetch bench_fetch 2>&1 | tail -2
echo "=== remote main now ==="
git rev-parse bench_fetch/main
echo "=== my HEAD ==="
git rev-parse HEAD
} > .b351_push.txt 2>&1
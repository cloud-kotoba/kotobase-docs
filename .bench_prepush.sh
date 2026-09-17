#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== FETCH ==="
git fetch net-kotobase main 2>&1
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== REMOTE net-kotobase/main ==="
git rev-parse net-kotobase/main
echo "=== REMOTE bench_fetch/main ==="
git rev-parse bench_fetch/main 2>&1
echo "=== STATUS tracked ==="
git status --short -- query-cosientist.md
} > /tmp/bench_prepush.txt 2>&1
echo done
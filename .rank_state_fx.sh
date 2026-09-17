#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== STATUS ==="
git status --short | head -60
echo "=== REMOTES ==="
git remote -v
echo "=== LOG ==="
git log --oneline -12
echo "=== FETCH ==="
git fetch bench_fetch 2>&1
echo "=== FETCH-DONE ==="
git log --oneline bench_fetch/main -6 2>&1
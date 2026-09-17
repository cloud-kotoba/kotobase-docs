#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== REMOTES ==="
git remote -v
echo "=== FETCH ==="
git fetch net-kotobase main 2>&1
echo "=== HEAD LOG ==="
git log --oneline -5 HEAD
echo "=== REV PARSE ==="
git rev-parse HEAD
git rev-parse net-kotobase/main
echo "=== STATUS ==="
git status --short
} > /tmp/bench_git.txt 2>&1
echo done
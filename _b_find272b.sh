#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== bench iter numbers ==="
grep -oE 'bench 第[0-9]+回' query-cosientist.md | awk -F'第' '{print $2}' | awk -F'回' '{print $1}' | sort -n | tail -5
echo "=== HEAD log ==="
git log --oneline -5
echo "=== is HEAD detached / branch ==="
git symbolic-ref -q HEAD || echo "detached"
echo "=== remote main ==="
git rev-parse --short origin/main 2>/dev/null
git rev-parse --short HEAD
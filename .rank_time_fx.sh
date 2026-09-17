#!/bin/bash
echo "=== DATE JST ==="
TZ='Asia/Tokyo' date '+%Y-%m-%d %H:%M:%S %Z'
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== FETCH bench_fetch ==="
git fetch bench_fetch 2>&1
echo "=== bench_fetch/main HEAD ==="
git rev-parse bench_fetch/main
echo "=== DIFF HEAD worktree ==="
git diff HEAD --stat -- query-cosientist.md
echo "=== adv/behind ==="
git rev-list --left-right --count HEAD...bench_fetch/main 2>&1
echo "=== newest first entry ==="
sed -n '404,405p' query-cosientist.md | cut -c1-90
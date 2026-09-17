#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD ==="
git rev-parse --short HEAD
echo "=== origin/main ==="
git rev-parse --short origin/main
echo "=== diff stat (tracked) ==="
git diff --stat query-cosientist.md
echo "=== untracked new measure files ==="
git status --short | grep -E '_b_run272|_b_stats272|_b_land272'
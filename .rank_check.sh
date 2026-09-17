#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== bench_fetch/main ==="
git rev-parse bench_fetch/main 2>/dev/null
echo "=== DIFF query-cosientist.md ==="
git diff HEAD --stat -- query-cosientist.md
echo "=== STATUS ==="
git status --short
} > .rank_check.out 2>&1

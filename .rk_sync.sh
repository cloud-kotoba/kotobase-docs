#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
{
echo "=== git fetch bench_fetch ==="
git fetch bench_fetch
echo "fetch_exit=$?"
echo "=== rev-parse HEAD ==="
git rev-parse HEAD
echo "=== rev-parse bench_fetch/main ==="
git rev-parse bench_fetch/main
echo "=== rev-parse origin/main ==="
git rev-parse origin/main 2>/dev/null
echo "origin_exit=$?"
echo "=== diff HEAD vs bench_fetch/main names ==="
git diff --name-only HEAD bench_fetch/main
echo "=== diff HEAD --stat -- query-cosientist.md (worktree uncommitted) ==="
git diff HEAD --stat -- query-cosientist.md
echo "numstat_end"
echo "=== status short ==="
git status --short
} > /tmp/rk_sync.log 2>&1
echo "log_written"

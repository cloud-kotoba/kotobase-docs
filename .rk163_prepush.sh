#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== refetch ==="
git fetch bench_fetch 2>&1 | head -3
echo "=== local HEAD ==="
git rev-parse HEAD
echo "=== remote bench_fetch ==="
git rev-parse bench_fetch 2>/dev/null || git rev-parse bench_fetch/main 2>/dev/null
echo "=== diff HEAD vs remote (should be empty if same) ==="
git rev-list --left-right --count HEAD...bench_fetch 2>/dev/null || echo "cannot compare"
echo "=== files changed vs HEAD ==="
git diff --stat HEAD -- query-cosientist.md | tail -3
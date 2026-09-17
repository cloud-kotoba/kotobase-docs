#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== GIT STATUS ==="
git status --short 2>&1 | head -50
echo "=== HEAD ==="
git rev-parse HEAD 2>&1
echo "=== DIFF HEAD query ==="
git diff HEAD --stat -- query-cosientist.md 2>&1
echo "=== FETCH ==="
git fetch bench_fetch 2>&1
echo "=== REMOTE HEAD bench_fetch ==="
git rev-parse bench_fetch/main 2>&1  # try main
git rev-parse bench_fetch/HEAD 2>&1
echo "=== HEAD vs remote ==="
git rev-parse HEAD 2>&1
echo "=== ITER LOG HEAD ENTRY ==="
grep -n 'rank 第' query-cosientist.md 2>&1 | head -5
echo "=== ITER LOG HEADER COUNT ==="
grep -c '^## Iteration log' query-cosientist.md 2>&1
echo "=== LAST 5 LOG LINES ==="
tail -30 query-cosientist.md 2>&1
} > .rank_probe.out 2>&1
echo "done"

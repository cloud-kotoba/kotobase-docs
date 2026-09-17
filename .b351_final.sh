#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== rank157 entry present in pushed HEAD? ==="
git show 13cbce4:query-cosientist.md | grep -c '^\- 2026-09-07: rank 第157回。14:59 JST tick'
echo "=== rank157 tail (run364) present? ==="
git show 13cbce4:query-cosientist.md | grep -c 'run ID は run364 使用'
echo "=== Iteration-log header count in HEAD ==="
git show 13cbce4:query-cosientist.md | grep -c '^## Iteration log'
echo "=== entry order (first 5 bullets after header) ==="
git show 13cbce4:query-cosientist.md | awk '/^## Iteration log/{f=1} f&&/^\- 2026-09-07:/{print $0}' | head -5 | cut -c1-55
echo "=== worktree status ==="
git status --short -- query-cosientist.md
echo "=== divergence check ==="
git rev-parse HEAD
git rev-parse bench_fetch/main
} > .b351_final.txt 2>&1
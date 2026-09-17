#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===COMMITTED HEAD top-of-iterlog (git show HEAD) first 6 lines from Iteration log==="
git show HEAD:query-cosientist.md | awk '/^## Iteration log$/{f=NR} f && NR>=f && NR<=f+3{print NR": "substr($0,1,80)}'
echo "===WORKTREE top-of-iterlog first 6 lines==="
awk '/^## Iteration log$/{f=NR} f && NR>=f && NR<=f+3{print NR": "substr($0,1,80)}' query-cosientist.md
echo "===FULL DIFF vs HEAD==="
git diff HEAD -- query-cosientist.md | head -40
echo "===NUMSTAT==="
git diff --numstat -- query-cosientist.md
echo "===HEAD refetch now==="
git fetch bench_fetch 2>&1 | tail -2
git rev-parse HEAD
git rev-parse bench_fetch/main 2>&1
} > _rk_diff.txt 2>&1
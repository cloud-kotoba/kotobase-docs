#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===NUMSTAT vs HEAD==="
git diff --numstat -- query-cosientist.md
echo "===HEADER COUNT==="
grep -c "^## Iteration log$" query-cosientist.md
echo "===TOP 3 ITER==="
awk '/^## Iteration log$/{f=NR} f && NR>=f && NR<=f+2{print NR": "substr($0,1,70)}' query-cosientist.md
echo "===DIFF check pure 1-line==="
git diff HEAD -- query-cosientist.md | grep -c "^+"
echo "===HEAD/remote==="
git rev-parse HEAD
git rev-parse bench_fetch/main 2>&1
echo "===DATE==="
date '+%Y-%m-%d %H:%M:%S'
} > _rk_v2.txt 2>&1
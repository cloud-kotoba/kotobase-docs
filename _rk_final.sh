#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===COMMITTED HEAD (pushed b12b0cf) top iter==="
git show HEAD:query-cosientist.md | awk '/^## Iteration log$/{f=NR} f && NR>=f && NR<=f+2{print NR": "substr($0,1,70)}'
echo "===HEADER COUNT in committed==="
git show HEAD:query-cosientist.md | grep -c "^## Iteration log$"
echo "===rank191 present in committed?==="
git show HEAD:query-cosientist.md | grep -c "^\- 2026-09-08: rank 第191回。"
echo "===clean?==="
git status --short -- query-cosientist.md
echo "===HEAD/remote==="
git rev-parse HEAD
git rev-parse bench_fetch/main 2>&1
} > _rk_final.txt 2>&1
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===HEADER COUNT==="
grep -c "^## Iteration log$" query-cosientist.md
echo "===NUMSTAT vs HEAD==="
git diff --numstat -- query-cosientist.md
echo "===TOP 5 ITER LINES==="
awk '/^## Iteration log$/{f=NR} f && NR>=f && NR<=f+3{print NR": "substr($0,1,60)}' query-cosientist.md
} > _rk_verify.txt 2>&1
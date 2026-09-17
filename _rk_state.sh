#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===HEAD now==="
git rev-parse HEAD
echo "===bench_fetch/main==="
git rev-parse bench_fetch/main 2>&1
echo "===LOG -6==="
git log --oneline -6
echo "===STATUS query-tracked==="
git status --short -- query-cosientist.md
echo "===NUMSTAT vs HEAD==="
git diff --numstat -- query-cosientist.md
echo "===DIFF vs HEAD (first 6 lines)==="
git diff HEAD -- query-cosientist.md | head -6
echo "===COMMITTED 3863ce6 top iter==="
git show 3863ce6:query-cosientist.md | awk '/^## Iteration log$/{f=NR} f && NR>=f && NR<=f+2{print NR": "substr($0,1,60)}'
echo "===which commit added falsify 192==="
git log --oneline --all -S "falsify 第192回" -- query-cosientist.md | head -5
} > _rk_state.txt 2>&1
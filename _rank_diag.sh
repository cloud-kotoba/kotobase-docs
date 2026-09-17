#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===REMOTES==="
git remote -v
echo "===DIF query-cosientist.md==="
git diff --stat query-cosientist.md
echo "===BENCH_FETCH LOG SINCE HEAD==="
git log --oneline HEAD..bench_fetch/main 2>&1
echo "===NETKOTO MAIN==="
git rev-parse net-kotobase/main 2>&1
echo "===BENCH_FETCH MAIN==="
git rev-parse bench_fetch/main 2>&1
echo "===31a65c9 SHOW==="
git show --stat 31a65c9 2>&1 | head -20
echo "===UNTRACKED COUNT (excluding state doc)==="
git status --porcelain | grep -c '^??'
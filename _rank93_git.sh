#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===DIFF query-cosientist.md (working vs HEAD)==="
git diff --stat query-cosientist.md
echo "===DIFF content==="
git diff query-cosientist.md | head -80
echo "===AHEAD/BEHIND==="
git fetch net-kotobase 2>&1
git log --oneline -1 net-kotobase/main 2>&1
echo "===local HEAD==="
git log --oneline -1
echo "===count c0da368 ancestors? check tip matches remote==="
git rev-list --count HEAD..net-kotobase/main 2>&1
echo "===stash list==="
git stash list 2>&1 | head
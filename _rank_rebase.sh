#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===REBASE merge dir==="
ls -la .git/rebase-merge/ 2>&1
echo "===done==="
cat .git/rebase-merge/done 2>&1
echo "===git-rebase-todo tail==="
tail -6 .git/rebase-merge/git-rebase-todo 2>&1
echo "===head-name==="
cat .git/rebase-merge/head-name 2>&1
echo "===onto==="
cat .git/rebase-merge/onto 2>&1
echo "===orig-head==="
cat .git/rebase-merge/orig-head 2>&1
echo "===index conflict?==="
git ls-files -u query-cosientist.md 2>&1 | head -10
echo "===conflict markers in file?==="
grep -n '^<<<<<<<\|^=======\|^>>>>>>>' query-cosientist.md 2>&1 | head -6
echo "===now==="
date "+%H:%M:%S"
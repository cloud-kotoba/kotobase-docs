#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===HEAD==="
git rev-parse HEAD 2>&1
echo "===MERGE_HEAD==="
cat .git/MERGE_HEAD 2>&1
echo "===REBASE dir==="
ls .git/rebase-merge 2>&1 | head -3
ls .git/rebase-apply 2>&1 | head -3
echo "===STATUS (non-untracked)==="
git status --short | grep -v '^??' 2>&1
echo "===LOG --all recent==="
git log --oneline -8 --all 2>&1 | head -12
echo "===LOG HEAD..net-kotobase/main==="
git log --oneline HEAD..net-kotobase/main 2>&1
echo "===MERGE_MSG==="
head -5 .git/MERGE_MSG 2>&1
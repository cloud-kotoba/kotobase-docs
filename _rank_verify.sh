#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===HEAD==="
git rev-parse --short HEAD 2>&1
echo "===STATUS non-untracked==="
git status --short | grep -v '^??' 2>&1
echo "===LOG -4==="
git log --oneline -4 2>&1
echo "===net-kotobase main==="
git rev-parse --short net-kotobase/main 2>&1
echo "===MERGE_HEAD?==="
test -f .git/MERGE_HEAD && echo PRESENT || echo none
echo "===rebase?==="
test -d .git/rebase-merge && echo PRESENT || echo none
echo "===now==="
date "+%H:%M:%S"
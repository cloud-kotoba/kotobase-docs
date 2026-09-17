#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===FULL STATUS==="
git status 2>&1 | head -12
echo "===REBASE DIR FYI==="
ls .git/rebase-merge/ 2>&1
echo "===REBASING?==="
git rev-parse --git-path rebase-merge 2>&1
echo "===HEAD NOW==="
git rev-parse --short HEAD 2>&1
echo "===pid of pending git?==="
ps aux 2>/dev/null | grep -iE 'git (merge|rebase|checkout|am)|rebase-merge' | grep -v grep | head -5
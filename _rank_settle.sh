#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===HEAD short==="
git rev-parse --short HEAD
echo "===abbrev ref==="
git rev-parse --abbrev-ref HEAD
echo "===FULL STATUS==="
git status
echo "===staged stat==="
git diff --cached --stat
echo "===UNSTAGED (worktree) stat==="
git diff --stat
echo "===net-kotobase main==="
git rev-parse --short net-kotobase/main
echo "===reflog -3==="
git reflog -3
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
echo "=== remotes ===" > /tmp/rank_git.txt
git remote -v >> /tmp/rank_git.txt 2>&1
echo "=== branch ===" >> /tmp/rank_git.txt
git branch -a >> /tmp/rank_git.txt 2>&1
echo "=== HEAD symbolic ===" >> /tmp/rank_git.txt
git symbolic-ref HEAD 2>&1 >> /tmp/rank_git.txt
echo "=== diff stat ===" >> /tmp/rank_git.txt
git diff --stat >> /tmp/rank_git.txt 2>&1
echo DONE >> /tmp/rank_git.txt
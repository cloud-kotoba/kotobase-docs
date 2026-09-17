#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "== HEAD =="
git rev-parse HEAD
echo "== STATUS =="
git status --short | head -40
echo "== BRANCH =="
git branch -a 2>&1 | head -20
echo "== REMOTE =="
git remote -v
echo "== LOG =="
git log --oneline -8
} > /tmp/rank_git1.txt 2>&1
echo done
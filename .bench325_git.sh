#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
exec > /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.bench325_git.txt 2>&1
echo "===STATUS==="
git status --short | grep -v '^??'
echo "===DIFFSTAT==="
git diff --stat
echo "===HEAD==="
git rev-parse HEAD
echo "===FETCHHEAD==="
git rev-parse net-kotobase/main FETCH_HEAD 2>/dev/null
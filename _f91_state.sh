#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "---FETCH---"
git fetch net-kotobase
echo "FETCH_EXIT=$?"
echo "---HEAD---"
git rev-parse HEAD
echo "---MAIN---"
git rev-parse net-kotobase/main
echo "---BRANCH---"
git branch -a
echo "---STATUS---"
git status --short
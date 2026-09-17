#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "---FETCH---"
git fetch net-kotobase 2>&1
echo "---HEAD---"
git rev-parse HEAD
echo "---REMOTE---"
git rev-parse net-kotobase/main
echo "---BRANCH---"
git branch --show-current
echo "---DATE---"
date "+%Y-%m-%d %H:%M:%S %Z"
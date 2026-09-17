#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== FETCH ===" >> .b329_git.txt
git fetch net-kotobase main >> .b329_git.txt 2>&1
echo "=== LOG ===" >> .b329_git.txt
git log --oneline -8 >> .b329_git.txt 2>&1
echo "=== DIFFSTAT remote ===" >> .b329_git.txt
git diff --stat HEAD net-kotobase/main >> .b329_git.txt 2>&1
echo "=== STATUS ===" >> .b329_git.txt
git status --short >> .b329_git.txt 2>&1
echo "=== DATE ===" >> .b329_git.txt
date '+%Y-%m-%d %H:%M:%S %Z' >> .b329_git.txt
echo "=== UPTIME ===" >> .b329_git.txt
uptime >> .b329_git.txt
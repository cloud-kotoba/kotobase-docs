#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== DATE ===" > /tmp/b328_git.txt
date '+%Y-%m-%d %H:%M:%S %Z' >> /tmp/b328_git.txt
echo "=== LOAD ===" >> /tmp/b328_git.txt
uptime >> /tmp/b328_git.txt
echo "=== FETCH ===" >> /tmp/b328_git.txt
git fetch origin 2>&1 >> /tmp/b328_git.txt
echo "=== HEAD ===" >> /tmp/b328_git.txt
git rev-parse HEAD >> /tmp/b328_git.txt
echo "=== REMOTE origin/main ===" >> /tmp/b328_git.txt
git rev-parse origin/main 2>&1 >> /tmp/b328_git.txt
echo "=== STATUS ===" >> /tmp/b328_git.txt
git status --short 2>&1 >> /tmp/b328_git.txt
echo "=== REMOTES ===" >> /tmp/b328_git.txt
git remote -v 2>&1 >> /tmp/b328_git.txt
echo "DONE"
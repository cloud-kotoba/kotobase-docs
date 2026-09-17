#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== DATE ==="
date
echo "=== GIT STATUS ==="
git status --short | head -40
echo "=== GIT LOG ==="
git log --oneline -8
echo "=== HOST LOAD ==="
uptime
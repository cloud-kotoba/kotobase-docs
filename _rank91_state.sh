#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
date
echo "===REMOTE==="
git remote -v
echo "===LOG==="
git log --oneline -6
echo "===STATUS==="
git status --short
echo "===LAST5LOG==="
git log --oneline -5 --format='%h %ci %s'
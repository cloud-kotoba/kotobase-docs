#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===PWD==="
pwd
echo "===HEAD==="
git rev-parse HEAD 2>&1
echo "===LOG==="
git log --oneline -6 2>&1
echo "===FETCH==="
git fetch --all 2>&1 | head -20
echo "===HEAD-AFTER-FETCH==="
git rev-parse HEAD 2>&1
echo "===LOG-AFTER-FETCH==="
git log --oneline -4 2>&1
echo "===UPSTREAM==="
git rev-parse @{u} 2>&1
echo "===AHEAD/BEHIND==="
git rev-list --left-right --count HEAD...@{u} 2>&1
echo "===STATUS==="
git status --short 2>&1
#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs 2>/dev/null || cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs 2>/dev/null || cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git pull --ff-only 2>&1
echo "===LOG top8==="
git log --oneline -8
echo "===STATUS==="
git status --short | head -30
echo "===REMOTE top==="
git fetch net-kotobase 2>&1
git log --oneline -1 net-kotobase/main 2>&1
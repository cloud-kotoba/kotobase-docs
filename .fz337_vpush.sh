#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase > /tmp/verify_push.txt 2>&1
echo "head=$(git rev-parse HEAD)" >> /tmp/verify_push.txt 2>&1
echo "remote_main=$(git rev-parse net-kotobase/main)" >> /tmp/verify_push.txt 2>&1
echo "worktree_clean=$(git status --porcelain query-cosientist.md | wc -l | tr -d ' ')" >> /tmp/verify_push.txt 2>&1
echo "run337A-C_count=$(grep -o 'run337A\u2013C' query-cosientist.md | wc -l | tr -d ' ')" >> /tmp/verify_push.txt 2>&1
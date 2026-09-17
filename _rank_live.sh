#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===RUNNING bot procs==="
ps aux 2>/dev/null | grep -iE 'rank|falsify|bench|cosient|_b7|_f[0-9]|_co|_rank' | grep -v grep | head -15
echo "===staged diff stat==="
git diff --cached --stat query-cosientist.md 2>&1
echo "===staged diff content (first 30 lines)==="
git diff --cached query-cosientist.md 2>&1 | head -30
echo "===reflog -5==="
git reflog -5 2>&1
echo "===now==="
date "+%H:%M:%S"
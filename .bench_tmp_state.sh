#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
{
echo "===DATE==="
date
date -u
echo "===UPTIME==="
uptime
echo "===PWD==="
pwd
echo "===GIT STATUS==="
git status --porcelain=v1 2>&1 | head -40
echo "===GIT LOG HEAD==="
git log --oneline -6 2>&1
echo "===REMOTE==="
git rev-parse HEAD 2>&1
git rev-parse net-kotobase/main 2>&1
echo "===GREP 深夜帯==="
grep -n "深夜帯" query-cosientist.md 2>&1 | tail -8
echo "===GREP 23時台==="
grep -n "23時台" query-cosientist.md 2>&1 | tail -8
echo "===GREP LAST NEXT lines==="
grep -n "^ *NEXT:" query-cosientist.md 2>&1 | tail -6
} > .bench_tmp_state.txt 2>&1
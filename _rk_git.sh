#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===DATE==="
date '+%Y-%m-%d %H:%M:%S %Z %z'
echo "===REMOTES==="
git remote -v
echo "===FETCH bench_fetch==="
git fetch bench_fetch 2>&1 | tail -5
echo "===HEAD==="
git rev-parse HEAD
echo "===bench_fetch/main==="
git rev-parse bench_fetch/main 2>&1
echo "===main local==="
git rev-parse main 2>&1
echo "===log oneline -8==="
git log --oneline -8
} > _rk_git.txt 2>&1
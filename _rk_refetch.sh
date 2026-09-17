#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
git fetch bench_fetch 2>&1 | tail -3
echo "===HEAD after refetch==="
git rev-parse HEAD
echo "===bench_fetch/main==="
git rev-parse bench_fetch/main 2>&1
echo "===log -4==="
git log --oneline -4
echo "===DATE==="
date '+%Y-%m-%d %H:%M:%S'
} > _rk_refetch.txt 2>&1
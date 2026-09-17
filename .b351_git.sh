#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== HEAD REV ==="
git rev-parse HEAD
git log --oneline -6
echo "=== DIFF STAT (query-cosientist.md) ==="
git diff --stat query-cosientist.md
echo "=== FETCH ==="
git fetch bench_fetch 2>&1 | tail -5
echo "=== FETCHED bench_fetch/main ==="
git rev-parse bench_fetch/main 2>&1
echo "=== date ==="
date
} > .b351_git.txt 2>&1
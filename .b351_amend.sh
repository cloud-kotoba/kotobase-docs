#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "=== amend ==="
git add query-cosientist.md
git commit --amend --no-edit
echo "=== log -3 ==="
git log --oneline -3
echo "=== fetch ==="
git fetch bench_fetch 2>&1 | tail -3
echo "=== my HEAD ==="
git rev-parse HEAD
echo "=== bench_fetch/main ==="
git rev-parse bench_fetch/main
} > .b351_amend.txt 2>&1
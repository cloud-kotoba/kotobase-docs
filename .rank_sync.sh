#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch
echo "---REV---"
git rev-parse HEAD
echo "---REMOTE---"
git rev-parse bench_fetch/main 2>/dev/null || git rev-parse bench_fetch/HEAD 2>/dev/null
echo "---DIFF---"
git diff HEAD --stat -- query-cosientist.md
echo "---STATUS---"
git status --short

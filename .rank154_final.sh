#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch > /dev/null 2>&1
echo "HEAD=$(git rev-parse HEAD)"
echo "BENCH_MAIN=$(git rev-parse bench_fetch/main)"
echo "DIFF_HEAD_TO_MAIN=$(git rev-list --count HEAD..bench_fetch/main)"
git log --oneline -5
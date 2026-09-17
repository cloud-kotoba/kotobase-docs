#!/usr/bin/env bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch 2>&1
echo "local=$HEAD_"
git rev-parse HEAD
git rev-parse bench_fetch/main
echo "---grep rank169 in working tree---"
grep -c 'rank 第169回。21:08' query-cosientist.md
echo "---hdr count---"
grep -c '^## Iteration log$' query-cosientist.md
echo "---top 3 entries tree---"
grep -oE '^- 2026-09-07: (rank|bench|cosientist|falsify) 第[0-9]+回' query-cosientist.md | head -3
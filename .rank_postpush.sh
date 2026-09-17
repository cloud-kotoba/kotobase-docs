#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch > /tmp/rank_postpush.txt 2>&1
echo "===LOCAL-HEAD===" >> /tmp/rank_postpush.txt
git rev-parse HEAD >> /tmp/rank_postpush.txt 2>&1
echo "===REMOTE-HEAD===" >> /tmp/rank_postpush.txt
git rev-parse bench_fetch/main >> /tmp/rank_postpush.txt 2>&1
echo "===RANK181-PRESENT===" >> /tmp/rank_postpush.txt
git show bench_fetch/main:query-cosientist.md | grep -c "rank 第181回。04:36 JST tick。" >> /tmp/rank_postpush.txt 2>&1
echo "===HEADER-COUNT-REMOTE===" >> /tmp/rank_postpush.txt
git show bench_fetch/main:query-cosientist.md | grep -c "^## Iteration log" >> /tmp/rank_postpush.txt 2>&1
echo "===ORDER-CHECK===" >> /tmp/rank_postpush.txt
git show bench_fetch/main:query-cosientist.md | sed -n '/^## Iteration log/,+3p' | grep -o "rank 第181回\|rank 第180回" | head -2 >> /tmp/rank_postpush.txt 2>&1
echo "===DONE===" >> /tmp/rank_postpush.txt
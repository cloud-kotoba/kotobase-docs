#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===PUSH===" >> /tmp/rank_push.txt
git push bench_fetch HEAD:main >> /tmp/rank_push.txt 2>&1
echo "PUSH-EXIT=$?" >> /tmp/rank_push.txt
echo "===LOCAL-HEAD===" >> /tmp/rank_push.txt
git rev-parse HEAD >> /tmp/rank_push.txt 2>&1
echo "===DONE===" >> /tmp/rank_push.txt
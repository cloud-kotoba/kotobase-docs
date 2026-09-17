#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push bench_fetch HEAD:main > .rank154_push.txt 2>&1
echo "PUSH_EXIT=$?" >> .rank154_push.txt
git rev-parse HEAD >> .rank154_push.txt
git rev-parse bench_fetch/main >> .rank154_push.txt 2>&1
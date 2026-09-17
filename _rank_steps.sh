#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git fetch net-kotobase > /tmp/rank_fetch.txt 2>&1
echo "fetch_rc=$?" >> /tmp/rank_fetch.txt
echo "HEAD=$(git rev-parse HEAD)" >> /tmp/rank_fetch.txt
echo "REMOTE=$(git rev-parse net-kotobase/main)" >> /tmp/rank_fetch.txt
echo "DIFF_LR=$(git rev-list --left-right --count HEAD...net-kotobase/main)" >> /tmp/rank_fetch.txt
echo "DATE=$(date)" >> /tmp/rank_fetch.txt
git log --oneline -10 >> /tmp/rank_fetch.txt 2>&1
echo "DONE" >> /tmp/rank_fetch.txt
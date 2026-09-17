#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git add query-cosientist.md
git commit -m "bench 第176回: K-Z3 20hr n-add run394 (cold 1/60 ~1.7% A 単発2.47s pos1, B/C+control 0 完全静穏分離成立, falsify run393 2/60 の8分後減弱; 20hr通算 10/180 ~5.6% low-to-mid 帯候補; NEXT run395)" > /tmp/.b394_commit.txt 2>&1
git push net-kotobase HEAD:main > /tmp/.b394_push.txt 2>&1
echo "commit:$(cat /tmp/.b394_commit.txt | head -3)"
echo "push:$(cat /tmp/.b394_push.txt | head -5)"
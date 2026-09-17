#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
# re-sync guard before push
git fetch net-kotobase > /tmp/push_pre.txt 2>&1
echo "head=$(git rev-parse HEAD)" >> /tmp/push_pre.txt 2>&1
echo "parent=$(git rev-parse HEAD^)" >> /tmp/push_pre.txt 2>&1
echo "remote_main=$(git rev-parse net-kotobase/main)" >> /tmp/push_pre.txt 2>&1
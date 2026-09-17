#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > /tmp/b385_push.txt 2>&1
echo "push rc=$?" >> /tmp/b385_push.txt
git fetch net-kotobase main >> /tmp/b385_push.txt 2>&1
git rev-parse net-kotobase/main >> /tmp/b385_push.txt 2>&1
echo done
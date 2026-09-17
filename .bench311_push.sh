#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD before push ===" >> /tmp/bench311_push.txt
git rev-parse HEAD >> /tmp/bench311_push.txt 2>&1
git push net-kotobase HEAD:main >> /tmp/bench311_push.txt 2>&1
echo "PUSH_RC=$?" >> /tmp/bench311_push.txt
echo "=== verify remote ===" >> /tmp/bench311_push.txt
git fetch net-kotobase main >> /tmp/bench311_push.txt 2>&1
git rev-parse net-kotobase/main >> /tmp/bench311_push.txt 2>&1
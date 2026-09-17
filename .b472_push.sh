#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > /tmp/b472_push.txt 2>&1
echo "PUSH_EXIT=$?" >> /tmp/b472_push.txt
git rev-parse net-kotobase/main >> /tmp/b472_push.txt
git rev-parse HEAD >> /tmp/b472_push.txt
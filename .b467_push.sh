#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > /tmp/b467_fetch.log 2>&1
git rev-parse net-kotobase/main > /tmp/b467_remote.txt 2>&1
git push net-kotobase HEAD:main > /tmp/b467_push.log 2>&1
echo pushed
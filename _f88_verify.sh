#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase > /tmp/f88_v.txt 2>&1
echo "LOCAL-HEAD: $(git rev-parse HEAD)"
echo "REMOTE-MAIN: $(git rev-parse net-kotobase/main)"
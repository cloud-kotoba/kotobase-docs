#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > /tmp/b467_f2.log 2>&1
git rev-parse HEAD > /tmp/b467_h2.txt 2>&1
git rev-parse net-kotobase/main > /tmp/b467_r2.txt 2>&1
echo ok
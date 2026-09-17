#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > .bench351_push.txt 2>&1
sleep 2
git fetch net-kotobase main > .bench351_posta_fetch.txt 2>&1
git rev-parse HEAD > .bench351_posta_head.txt 2>&1
git rev-parse net-kotobase/main > .bench351_posta_remote.txt 2>&1
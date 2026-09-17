#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git reset --hard net-kotobase/main > .bench329_reset.txt 2>&1
echo "reset_rc=$?" >> .bench329_reset.txt
git rev-parse HEAD >> .bench329_reset.txt 2>&1
git status --short query-cosientist.md >> .bench329_reset.txt 2>&1
grep -c 'run329' query-cosientist.md > .bench329_rc329.txt 2>&1
echo "reset_done" >> .bench329_reset.txt
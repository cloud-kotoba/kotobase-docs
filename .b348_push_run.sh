#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== push net-kotobase ===" > .b348_push.txt
git push net-kotobase HEAD:main >> .b348_push.txt 2>&1
echo "rc=$?" >> .b348_push.txt
echo "=== head ===" >> .b348_push.txt
git rev-parse HEAD >> .b348_push.txt 2>&1
echo "=== remote net-kotobase/main ===" >> .b348_push.txt
git rev-parse net-kotobase/main >> .b348_push.txt 2>&1
echo "=== fetch bench_fetch ===" >> .b348_push.txt
git fetch bench_fetch main >> .b348_push.txt 2>&1
echo "rc=$?" >> .b348_push.txt
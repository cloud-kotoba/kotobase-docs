#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b345_gs.txt
echo "=== NOW ===" > $R
date '+%H:%M:%S %Z' >> $R
echo "=== FETCH net-kotobase ===" >> $R
git fetch net-kotobase >> $R 2>&1; echo "rc=$?" >> $R
echo "=== HEAD ===" >> $R
git rev-parse HEAD >> $R 2>&1
echo "=== net-kotobase/main ===" >> $R
git rev-parse net-kotobase/main >> $R 2>&1
echo "=== log -5 ===" >> $R
git log --oneline -6 >> $R 2>&1
echo "=== status query-cosientist.md ===" >> $R
git status --short query-cosientist.md >> $R 2>&1
echo "DONE" >> $R
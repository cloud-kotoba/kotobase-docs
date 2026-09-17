#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b347_final.txt
git fetch net-kotobase > /tmp/b347_fet.txt 2>&1; echo "fetch rc=$?" > $R
echo "=== HEAD ===" >> $R
git rev-parse HEAD >> $R 2>&1
echo "=== main ===" >> $R
git rev-parse net-kotobase/main >> $R 2>&1
echo "=== run347 on main? ===" >> $R
git show net-kotobase/main:query-cosientist.md | grep -c "run347" >> $R 2>&1
echo "=== 第161回 on main? ===" >> $R
git show net-kotobase/main:query-cosientist.md | grep -c "第161回" >> $R 2>&1
echo "DONE" >> $R
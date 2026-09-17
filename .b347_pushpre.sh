#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b347_pushpre.txt
echo "=== HEAD ===" > $R
git rev-parse HEAD >> $R 2>&1
echo "=== HEAD^ ===" >> $R
git rev-parse HEAD^ >> $R 2>&1
echo "=== main ===" >> $R
git rev-parse net-kotobase/main >> $R 2>&1
echo "=== ancestor check HEAD^ is ancestor of main? ===" >> $R
git merge-base --is-ancestor HEAD^ net-kotobase/main; echo "rc=$?" >> $R
echo "=== is HEAD ancestor of main? (should be 1=no, we're ahead) ===" >> $R
git merge-base --is-ancestor HEAD net-kotobase/main; echo "rc=$?" >> $R
echo "=== rev-list main..HEAD ===" >> $R
git rev-list --count net-kotobase/main..HEAD >> $R 2>&1
echo "DONE" >> $R
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b347_gs2.txt
date '+%H:%M:%S %Z' > $R
echo "=== FETCH ===" >> $R
git fetch net-kotobase >> $R 2>&1; echo "rc=$?" >> $R
echo "=== HEAD ===" >> $R
git rev-parse HEAD >> $R 2>&1
echo "=== main ===" >> $R
git rev-parse net-kotobase/main >> $R 2>&1
echo "=== log -3 ===" >> $R
git log --oneline -3 >> $R 2>&1
echo "=== does HEAD contain bench149 entry in iter-log? ===" >> $R
git show HEAD:query-cosientist.md 2>/dev/null | grep -c "第149回" >> $R 2>&1
echo "DONE" >> $R
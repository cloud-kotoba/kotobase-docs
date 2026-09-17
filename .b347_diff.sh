#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b347_diff.txt
echo "=== diff stat ===" > $R
git diff --stat query-cosientist.md >> $R 2>&1
echo "=== diff (first 3000) ===" >> $R
git diff --unified=1 query-cosientist.md | head -c 3000 >> $R 2>&1
echo "" >> $R
echo "=== log -3 ===" >> $R
git log --oneline -3 >> $R 2>&1
echo "=== HEAD vs main ===" >> $R
git rev-parse HEAD >> $R 2>&1
git rev-parse net-kotobase/main >> $R 2>&1
echo "DONE" >> $R
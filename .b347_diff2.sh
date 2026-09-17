#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
R=/tmp/b347_diff2.txt
echo "=== diff stat ===" > $R
git diff --stat >> $R 2>&1
echo "=== diff query-cosientist only (lines changed) ===" >> $R
git diff --unified=0 query-cosientist.md >> $R 2>&1
echo "=== status ===" >> $R
git status --short query-cosientist.md >> $R 2>&1
echo "DONE" >> $R
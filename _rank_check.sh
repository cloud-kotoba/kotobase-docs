#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
echo "=== rank block header ===" > /tmp/rank_check.txt
grep -n "期待 gain" query-cosientist.md >> /tmp/rank_check.txt 2>&1
echo "=== run235 in rank block (lines 130-240) ===" >> /tmp/rank_check.txt
sed -n '135,240p' query-cosientist.md | grep -n "run235\|run236\|19時台" >> /tmp/rank_check.txt 2>&1
echo "=== Iteration log header (first 3 lines) ===" >> /tmp/rank_check.txt
sed -n '281,283p' query-cosientist.md >> /tmp/rank_check.txt 2>&1
echo "DONE" >> /tmp/rank_check.txt
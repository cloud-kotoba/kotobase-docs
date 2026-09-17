#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
grep -n "rank 第154回。" query-cosientist.md > .rank154_verify.txt 2>&1
echo "---count---" >> .rank154_verify.txt
grep -c "rank 第154回。" query-cosientist.md >> .rank154_verify.txt 2>&1
echo "---30... "None" lines 35-46 head of log---" >> .rank154_verify.txt
awk 'NR>=360 && NR<=370' query-cosientist.md | cut -c1-80 >> .rank154_verify.txt
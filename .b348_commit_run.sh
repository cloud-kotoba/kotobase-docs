#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== add only query-cosientist.md ===" > .b348_commit.txt
git add query-cosientist.md >> .b348_commit.txt 2>&1
echo "=== staged ===" >> .b348_commit.txt
git diff --cached --name-only >> .b348_commit.txt 2>&1
echo "=== commit ===" >> .b348_commit.txt
git commit -m "bench 第149回: K-Z3 12時台 run348 n積み増し (cold 0/60, sibling run347A heavy の約3分後 quiet — 帯内1窓即消失短時間減弱の追加観測) + iterlog" >> .b348_commit.txt 2>&1
echo "rc=$?" >> .b348_commit.txt
echo "=== log ===" >> .b348_commit.txt
git log --oneline -2 >> .b348_commit.txt 2>&1
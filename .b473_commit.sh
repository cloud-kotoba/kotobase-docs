#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "bench 197: K-Z3 14h n-add run473 cold 8/60 ~13.3% (run473A heavy 6/20 14h初 heavy; control borderline 2/20; 14h total 19/240 ~7.9% 4set)" > /tmp/b473_commit.txt 2>&1
git rev-parse HEAD >> /tmp/b473_commit.txt 2>&1
git push net-kotobase HEAD:main >> /tmp/b473_commit.txt 2>&1
echo "PUSH_DONE rc=$?" >> /tmp/b473_commit.txt 2>&1
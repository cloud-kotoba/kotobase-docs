#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "bench 196: K-Z3 14h n-add run472 cold 5/60 ~8.3% (run472A cluster 5/20 即消失; 14h total 11/180 ~6.1% 3set; control 分離成立)" > /tmp/b472_commit.txt 2>&1
echo "COMMIT_EXIT=$?" >> /tmp/b472_commit.txt
git rev-parse HEAD >> /tmp/b472_commit.txt
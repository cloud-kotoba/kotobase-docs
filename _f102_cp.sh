#!/bin/sh
# commit + push falsify 第102回 run233 evidence
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "falsify 第102回: K-Z3 18時台 run233A-C (cold 5/60 ~8.3%, control borderline not-separated, 18時台通算 18/240 ~7.5%) + iteration log" > /tmp/_f102_commit.txt 2>&1
echo "commit rc=$?" >> /tmp/_f102_commit.txt
git push net-kotobase HEAD:main > /tmp/_f102_push.txt 2>&1
echo "push rc=$?" >> /tmp/_f102_push.txt
echo done
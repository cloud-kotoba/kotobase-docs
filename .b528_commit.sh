#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "bench 第233回: K-Z3 3時台 run528 n 積み増し (cold 1/60, control 分離成立)" > /tmp/b528_commit.log 2>&1
echo "commit_rc=$?" >> /tmp/b528_commit.log
git log --oneline -1 >> /tmp/b528_commit.log 2>&1
git push net-kotobase HEAD:main >> /tmp/b528_commit.log 2>&1
echo "push_rc=$?" >> /tmp/b528_commit.log
git rev-parse HEAD >> /tmp/b528_commit.log 2>&1
git rev-parse net-kotobase/main >> /tmp/b528_commit.log 2>&1
echo done
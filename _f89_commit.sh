#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md _f89_run215.sh _f89_analyze.py _f89_append.py > _f89_commit.txt 2>&1
git -c user.name="falsify" -c user.email="falsify@localhost" commit -m "falsify 第89回: K-Z3 15時台 n 積み増し run215A-C (cold 2/60)" >> _f89_commit.txt 2>&1
echo "commit rc=$?" >> _f89_commit.txt
git push net-kotobase HEAD:main >> _f89_commit.txt 2>&1
echo "push rc=$?" >> _f89_commit.txt
git rev-parse HEAD >> _f89_commit.txt
git rev-parse net-kotobase/main >> _f89_commit.txt
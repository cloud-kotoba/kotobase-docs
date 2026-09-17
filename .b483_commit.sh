#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "bench 第210回: K-Z3 16時台 n-add run484 cold 2/60 ~3.3% (run483 falsify先行->run484 読替; control 0/20 静穏分離成立; 16時台通算 27/360 ~7.5% 6set) evidence+iter-log" > /tmp/t_bs483_commit.log 2>&1
git push net-kotobase HEAD:main > /tmp/t_bs483_push.log 2>&1
echo "commit_rc=$?" > /tmp/t_bs483_commit_rc.log
echo "push_rc=$?" >> /tmp/t_bs483_commit_rc.log
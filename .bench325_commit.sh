#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
exec > /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.bench325_commit.txt 2>&1
git add query-cosientist.md
git commit -m "bench 137: K-Z3 7時台 run325A-C n-add cold 1/60 (run325A 単発散発 1.594s, B/C+CTRL 0/20 control分離成立, host load 171 extreme gate-exempt production HTTP); 7時台通算はrank判定に委ねる; status/rank to rank"
echo "===COMMIT DONE==="
git rev-parse HEAD
echo "===PUSH==="
git push net-kotobase HEAD:main 2>&1
echo "===PUSH RC $?==="
git rev-parse net-kotobase/main
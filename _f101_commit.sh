#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "---status---"
git status --short | grep -E "query-cosientist|_f101" 
echo "---add+commit---"
git add query-cosientist.md
git commit -m "falsify 第101回: K-Z3 18時台 run232A-C (run232A heavy cold 9/20, control 分離成立, 18時台通算 13/180 ~7.2% へ上振れ) + iteration log" 
echo "COMMIT_EXIT=$?"
echo "---new HEAD---"
git rev-parse HEAD
echo "---push---"
git push net-kotobase HEAD:main
echo "PUSH_EXIT=$?"
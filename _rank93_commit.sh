#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add -- query-cosientist.md
echo "===staged==="
git diff --cached --stat
echo "===commit==="
git commit -m "rank 第93回: falsify 第96回 run225 (16時台 cold 2/60) 取り込み, 16時台通算 8/360 ~2.2% 低位帯, rank 順位変動なし, NEXT K-Z3 17時台" 2>&1
echo "===log==="
git log --oneline -2
echo "===push==="
git push net-kotobase HEAD:main 2>&1 || git push net-kotobase HEAD 2>&1
echo "EXIT done"
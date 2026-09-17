#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git add query-cosientist.md
git -c user.name="net-kotobase-rank" -c user.email="jun784@gmail.com" commit -m "rank 第102回: bench 第92回 run236 (19時台 3セット目 2/60, control 分離成立で run235 borderline 補完) 取り込み, 19時台通算 12/180 ~6.7%, status遷移なし, 順位変動なし, NEXT K-Z3 19時台/20時台" > /tmp/rank_commit.txt 2>&1
echo "commit_rc=$?" >> /tmp/rank_commit.txt
echo "=== push ===" >> /tmp/rank_commit.txt
git push net-kotobase HEAD:main >> /tmp/rank_commit.txt 2>&1
echo "push_rc=$?" >> /tmp/rank_commit.txt
echo "=== post-push verify ===" >> /tmp/rank_commit.txt
echo "HEAD=$(git rev-parse HEAD)" >> /tmp/rank_commit.txt
git fetch net-kotobase >> /tmp/rank_commit.txt 2>&1
echo "REMOTE=$(git rev-parse net-kotobase/main)" >> /tmp/rank_commit.txt
echo "DIFF=$(git rev-list --left-right --count HEAD...net-kotobase/main)" >> /tmp/rank_commit.txt
echo DONE >> /tmp/rank_commit.txt
#!/usr/bin/env bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "rank 第169回: fold falsify169-run395(7/60)+cosientist128-run395(0/60 indep)+bench177-run396(3/60) -> K-Z3 20hr 6-set 20/360 ~5.6% mid-low; status/rank/evolve unchanged; NEXT K-Z3 21hr band-first run397"
echo "commit_rc=$?"
git rev-parse HEAD
git push bench_fetch HEAD:main 2>&1
echo "push_rc=$?"
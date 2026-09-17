#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "rank 第163回: fold bench169-run383 -> K-Z3 18hr(9/7) 3-set 13/180 ~7.2% 中位帯候補(17hr 27/360 ~7.5% と同水準, control 0/20 分離成立, 帯内1窓即消失継続); rank順位/status/evolve不変(K-Q1>K-Z2>K-Z3>K-S1>K-S2); NEXT K-Z3 18hr n-add run384"
echo "== commit done rc=$? =="
git push bench_fetch HEAD:main 2>&1 | tail -5
echo "== push done rc=$? =="
git rev-parse HEAD
git rev-parse bench_fetch
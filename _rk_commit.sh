#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===ADD+COMMIT==="
git add query-cosientist.md
git commit -m "rank 191st: fold falsify192-run434 -> 7hr 5/240 ~2.1% 4-set low band; status/rank/evolve unchanged; NEXT K-Z3 7hr n-add run435" 2>&1 | tail -5
echo "===NEW HEAD==="
git rev-parse HEAD
echo "===PUSH bench_fetch HEAD:main==="
git push bench_fetch HEAD:main 2>&1 | tail -8
echo "===AFTER PUSH bench_fetch/main==="
git rev-parse bench_fetch/main 2>&1
} > _rk_commit.txt 2>&1
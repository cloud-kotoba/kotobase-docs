#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
  echo "=== add ==="
  git add query-cosientist.md 2>&1; echo "add:$?"
  echo "=== commit ==="
  git commit -m "rank 第187回: fold bench189-run426 + falsify188-run427 -> 6時台 3/180 ~1.7% 低〜中位帯候補確定側; status/rank/evolve unchanged; NEXT K-Z3 6時台 n-add run428" 2>&1; echo "commit:$?"
  echo "=== new HEAD ==="
  git rev-parse HEAD 2>&1
  echo "=== push HEAD:main to bench_fetch ==="
  timeout 60 git push bench_fetch HEAD:main 2>&1; echo "push:$?"
  echo "=== bench_fetch after ==="
  git rev-parse bench_fetch 2>&1
} > .rank_commit_out.txt 2>&1
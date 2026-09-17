#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== pre-fetch HEAD/remote check ==="
  git fetch net-kotobase 2>&1 | tail -2
  echo "HEAD=$(git rev-parse HEAD)"
  echo "REMOTE=$(git rev-parse net-kotobase/main 2>&1)"
  echo "=== staged diff stat (only query-cosientist.md) ==="
  git diff --stat query-cosientist.md
  echo "=== commit ==="
  git add query-cosientist.md
  git commit -m "falsify 148: K-Z3 7时台 n-add run321A-C cold 3/60 (A 2/20 1.1354/1.5251s 散发 + B 1/20 0.5174s 境界值 single, C 0/20; CTRL 0/20 完全静稳 分离成立, cold search 局在, host load 58.94 borderline p50 upshift, heavy run271A non-reproduced 47-set; 7时台 通算 7/240 ~2.9% 低位带, traffic-independence counter-evidence; status/rank to rank)" 2>&1 | tail -5
  echo "=== commit HEAD ==="
  echo "NEWHEAD=$(git rev-parse HEAD)"
  echo "=== push HEAD:main ==="
  git push net-kotobase HEAD:main 2>&1 | tail -8
  echo "PUSH_RC=$?"
  echo "=== post-push verify ==="
  git fetch net-kotobase 2>&1 | tail -2
  echo "HEAD=$(git rev-parse HEAD)"
  echo "REMOTE=$(git rev-parse net-kotobase/main 2>&1)"
} > .f_commit.txt 2>&1
#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_rank87_commit.txt
{
  git add query-cosientist.md
  echo "add_rc=$?"
  git commit -m "rank 第87回: K-Q1 切れ手(cacao_b64)収束維持+14時台 10/180 ~5.6% 取り込み, NEXT cacao_b64 harness / K-Z3 15時台" 2>&1
  echo "commit_rc=$?"
  git push net-kotobase HEAD:main 2>&1
  echo "push_rc=$?"
  echo "---HEAD---"
  git rev-parse HEAD
  git log --oneline -2 2>&1
} >> "$OUT" 2>&1
cat "$OUT"
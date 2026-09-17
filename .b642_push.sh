#!/bin/zsh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "--- pre-push fetch ---"
  git fetch net-kotobase 2>&1
  echo "HEAD:    $(git rev-parse HEAD)"
  echo "remote:  $(git rev-parse net-kotobase/main)"
  echo "--- status (porcelain, tracked only) ---"
  git status --porcelain -- query-cosientist.md
  echo "--- commit ---"
  git add query-cosientist.md
  git commit -m "falsify 9/16 tick: K-Z3 15時台 run642A-C evidence (21/60 35.0%, control 分離成立) + iter entry (9/16 連続番号, 9/7 の旧第158回とは別)" 2>&1
  echo "post-commit HEAD: $(git rev-parse HEAD)"
  echo "--- push ---"
  git push net-kotobase HEAD:main 2>&1
  echo "--- post-push verify ---"
  git fetch net-kotobase 2>&1
  echo "HEAD:    $(git rev-parse HEAD)"
  echo "remote:  $(git rev-parse net-kotobase/main)"
} > /tmp/push_out.txt 2>&1
exit 0

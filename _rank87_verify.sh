#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_rank87_verify.txt
{
  git fetch net-kotobase 2>&1
  echo "fetch_rc=$?"
  echo "---MAIN---"
  git rev-parse net-kotobase/main
  echo "---MY COMMIT---"
  git rev-parse b430f97
  echo "---GIT STATUS (tracked)---"
  git status --short query-cosientist.md 2>&1
} >> "$OUT" 2>&1
cat "$OUT"
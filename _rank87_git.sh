#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_rank87_git.txt
rm -f "$OUT"
{
  echo "TIME: $(date '+%Y-%m-%d %H:%M:%S %Z')"
  echo "---FETCH---"
  git fetch net-kotobase 2>&1
  echo "fetch_rc=$?"
  echo "---HEAD---"
  git rev-parse HEAD
  echo "---MAIN---"
  git rev-parse net-kotobase/main
  echo "---AB (left=HEAD vs right=main count)---"
  git rev-list --count --left-right HEAD...net-kotobase/main 2>&1
  echo "---ANCESTOR (rc0 means HEAD ancestor of main)---"
  git merge-base --is-ancestor HEAD net-kotobase/main 2>&1
  echo "ancestor_rc=$?"
  echo "---STATUS---"
  git status --short 2>&1 | head -40
  echo "---LASTCOMMITS---"
  git log --oneline -5 2>&1
} >> "$OUT" 2>&1
cat "$OUT"
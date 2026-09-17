#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== fetch net-kotobase ==="
  git fetch net-kotobase 2>&1 | tail -5; echo "rc=$?"
  echo "=== HEAD (local) ==="
  git rev-parse HEAD 2>&1
  echo "=== net-kotobase/main ==="
  git rev-parse net-kotobase/main 2>&1
  echo "=== log top 6 ==="
  git log --oneline -6 2>&1
  echo "=== status query-cosientist.md ==="
  git status -s query-cosientist.md 2>&1
  echo "=== diffstat vs net-kotobase/main ==="
  git rev-list --left-right --count net-kotobase/main...HEAD 2>&1
} > /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.co_recheck.txt 2>&1
echo done
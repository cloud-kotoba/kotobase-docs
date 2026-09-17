#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "DATE: $(date '+%Y-%m-%d %H:%M:%S %Z')"
  echo "UPTIME: $(uptime)"
  echo "--- git log oneline -12 ---"
  git log --oneline -12
  echo "--- iter-log top lines (first 3 after header) ---"
  git show HEAD:query-cosientist.md | sed -n '/## Iteration log/,+3p'
} > /tmp/b_state2.txt 2>&1
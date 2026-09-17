#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "===== iter-log line 407-408 (should be my 212 first) ====="
  sed -n '407p' query-cosientist.md | cut -c1-90
  echo "===== K-Z3 row check: last 200 chars of L279 ====="
  awk 'NR==279{print substr($0,length($0)-220)}' query-cosientist.md
  echo "===== run487 count now ====="
  grep -c "run487" query-cosientist.md
  echo "===== run488 mention check ====="
  grep -c "run488" query-cosientist.md
} > /tmp/b487verify.txt 2>&1
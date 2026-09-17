#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "===== last 4 lines (with line numbers) ====="
  awk 'END{for(i=NR-3;i<=NR;i++) print i": "substr($0,1,180)}' query-cosientist.md
  echo "===== total lines ====="
  wc -l < query-cosientist.md
  echo "===== line 405 content prefix ====="
  sed -n '405p' query-cosientist.md | cut -c1-150
  echo "===== line 406-407 prefix ====="
  sed -n '406p;407p' query-cosientist.md | cut -c1-120
} > /tmp/tail.txt 2>&1
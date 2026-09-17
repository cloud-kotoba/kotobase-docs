#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_stat.txt
python3 .b479_parse.py > "$OUT" 2>&1
python3 .b479_stats.py >> "$OUT" 2>&1
{
  echo "=== elapsed ==="
  cat .b479_t0.txt
  cat /tmp/kb_smoke.txt
} >> "$OUT" 2>&1
echo done
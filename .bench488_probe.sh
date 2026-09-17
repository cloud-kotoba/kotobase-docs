#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
F=query-cosientist.md
OUT=.bench488_probe.txt
{
  echo "===== ITER LOG HEADER ====="
  grep -n "## Iteration log" "$F"
  echo "===== K-Z3 row ====="
  grep -n "^| K-Z3 |" "$F"
  echo "===== last 5 lines of file ====="
  tail -5 "$F"
} > "$OUT" 2>&1
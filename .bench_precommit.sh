#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_precommit.txt
{
  echo "=== date ==="
  date '+%Y-%m-%d %H:%M:%S %Z'
  echo "=== git status short (only md + db479) ==="
  git status --short | grep -E 'query-cosientist|b479'
  echo "=== K-Z3 row line ==="
  grep -n "^| K-Z3 | worker |" query-cosientist.md
  echo "=== iter log header line ==="
  grep -n "## Iteration log" query-cosientist.md
} > "$OUT" 2>&1
echo done
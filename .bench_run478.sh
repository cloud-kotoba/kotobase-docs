#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_r478.txt
{
  echo "=== run478 refs in doc ==="
  grep -c "run478" query-cosientist.md
  echo "=== run477 / run476 refs ==="
  grep -c "run477" query-cosientist.md
  grep -c "run476" query-cosientist.md
  echo "=== exact working diff vs HEAD ==="
  git diff query-cosientist.md
  echo "=== .b478 scratch files present? ==="
  ls -la .b478_* 2>&1 | head -20
} > "$OUT" 2>&1
echo done
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.rank_tick.out
{
  echo "=== git diff HEAD --stat (query-cosientist.md) ==="
  git diff HEAD --stat -- query-cosientist.md
  echo "=== git status short ==="
  git status --short | head -40
  echo "=== HEAD ==="
  git rev-parse HEAD
  echo "=== NEXT (last iter entry) ==="
  grep -n "NEXT:" query-cosientist.md | head -5
  echo "=== rank 第 (header + log) ==="
  grep -n "rank 第" query-cosientist.md | head -10
  echo "=== Iteration log header count ==="
  grep -c "^## Iteration log" query-cosientist.md
  echo DONE
} > "$OUT" 2>&1
echo "exit=$?" >> "$OUT"

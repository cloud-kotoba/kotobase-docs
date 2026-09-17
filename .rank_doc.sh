#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
  echo "=== log since rank186 ==="
  git log --oneline 52d4a33^..HEAD 2>&1
  echo "=== show bench189th message ==="
  git log -1 --format='%s%n%b' 871b712 2>&1
  echo "=== iterlog first/head entries ==="
  grep -n '## Iteration log' query-cosientist.md 2>&1
  echo "=== rank header line ==="
  grep -n 'rank 第' query-cosientist.md | head -5 2>&1
  echo "=== NEXT entries ==="
  grep -n 'NEXT: K-' query-cosientist.md | head -5 2>&1
} > .rank_doc_out.txt 2>&1
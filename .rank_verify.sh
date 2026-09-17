#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
  echo "=== numstat ==="
  git diff HEAD --numstat -- query-cosientist.md 2>&1
  echo "=== diffstat ==="
  git diff HEAD --stat -- query-cosientist.md 2>&1
  echo "=== header count now ==="
  grep -c '^## Iteration log' query-cosientist.md 2>&1
  echo "=== entry order (first 4 iter lines) ==="
  grep -nE '^## Iteration log|rank 第187回|falsify 第188回|bench 第189回' query-cosientist.md | head -6 2>&1
} > .rank_verify.txt 2>&1
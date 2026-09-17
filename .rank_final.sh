#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
  echo "=== remote HEAD ==="
  git rev-parse bench_fetch 2>&1
  echo "=== grep rank 第187回 in HEAD blob ==="
  git show HEAD:query-cosientist.md 2>&1 | grep -c 'rank 第187回。06:35' 2>&1
  echo "=== grep rank 第187回 in local worktree ==="
  grep -c 'rank 第187回。06:35' query-cosientist.md 2>&1
  echo "=== header count in HEAD blob ==="
  git show HEAD:query-cosientist.md 2>&1 | grep -c '^## Iteration log' 2>&1
  echo "=== diff HEAD worktree stat (should be empty) ==="
  git diff HEAD --stat -- query-cosientist.md 2>&1; echo "diff:$?"
} > .rank_final.txt 2>&1
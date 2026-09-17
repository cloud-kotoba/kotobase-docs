#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
  echo "=== HEAD ==="
  git rev-parse HEAD 2>&1
  echo "=== fetch bench_fetch ==="
  timeout 40 git fetch bench_fetch 2>&1; echo "fetch:$?"
  echo "=== bench_fetch ==="
  git rev-parse bench_fetch 2>&1
  echo "=== log -4 oneline ==="
  git log --oneline -4 2>&1
  echo "=== diff HEAD worktree stat ==="
  git diff HEAD --stat -- query-cosientist.md 2>&1; echo "diff:$?"
  echo "=== HEAD blob: first 6 iter-log lines (grep top entries) ==="
  git show HEAD:query-cosientist.md 2>&1 | grep -m6 -n 'Iteration log\|第188回\|第189回\|第186回' 2>&1
  echo "=== worktree: first iter-log lines ==="
  grep -m4 -n '第188回\|第189回\|第186回' query-cosientist.md 2>&1
} > .rank_state2.txt 2>&1
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "===== run487 count ====="
  grep -c "run487" query-cosientist.md
  echo "===== run488 count ====="
  grep -c "run488" query-cosientist.md
  echo "===== K-Z3 row line number ====="
  grep -n "^| K-Z3 |" query-cosientist.md | cut -d: -f1
  echo "===== HEAD vs remote ====="
  git rev-parse HEAD
  git rev-parse net-kotobase/main
  echo "===== worktree kz3 dirty? ====="
  git diff --stat query-cosientist.md
} > /tmp/b487v.txt 2>&1
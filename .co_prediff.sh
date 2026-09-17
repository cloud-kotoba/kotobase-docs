#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== diff stat ==="
  git diff --stat query-cosientist.md 2>&1
  echo "=== diff (first 12 lines) ==="
  git diff query-cosientist.md 2>&1 | head -14
} > /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.co_prediff.txt 2>&1
echo done
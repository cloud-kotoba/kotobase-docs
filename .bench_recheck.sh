#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_recheck.txt
git fetch net-kotobase main > /tmp/kb_re_fetch.txt 2>&1
{
  echo "=== HEAD ==="
  git rev-parse HEAD
  echo "=== remote main ==="
  git rev-parse net-kotobase/main
  echo "=== git status md only ==="
  git status --short | grep query-cosientist
  echo "=== git log tail 10 ==="
  git log --oneline -10
  echo "=== run479/478/477 in work row? ==="
  grep -o 'run479[^ ,；）。]*' query-cosientist.md | head
  grep -c "run478" query-cosientist.md
  grep -c "run479" query-cosientist.md
} > "$OUT" 2>&1
echo done
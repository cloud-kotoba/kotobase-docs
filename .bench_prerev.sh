#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_prerev.txt
git fetch net-kotobase main > /tmp/kb_pr_fetch.txt 2>&1
{
  echo "=== local HEAD ==="
  git rev-parse HEAD
  echo "=== remote main ==="
  git rev-parse net-kotobase/main
  echo "=== local diff vs remote (ahead count) ==="
  git rev-list --count HEAD..net-kotobase/main 2>/dev/null
} > "$OUT" 2>&1
echo done
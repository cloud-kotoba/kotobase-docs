#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_postpush.txt
git fetch net-kotobase main > /tmp/kb_pp_fetch.txt 2>&1
{
  echo "=== remote main after push ==="
  git rev-parse net-kotobase/main
  echo "=== my commit ==="
  git rev-parse HEAD
  echo "=== log -3 ==="
  git log --oneline -3
} > "$OUT" 2>&1
echo done
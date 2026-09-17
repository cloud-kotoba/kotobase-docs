#!/bin/bash
# bench tick - write state into a file, then read back
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_state.txt
{
  echo "=== HEAD ==="
  git rev-parse HEAD
  echo "=== REMOTE ==="
  git ls-remote net-kotobase main 2>&1 | head -3
  echo "=== HEAD:main ==="
  git rev-parse HEAD:main 2>&1
} > "$OUT" 2>&1
echo "written"

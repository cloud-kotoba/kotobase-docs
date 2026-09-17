#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/kb_head.txt
{
  echo "=== HEAD commit ==="
  git log -1 --oneline
  echo "=== working file bytes ==="
  wc -c query-cosientist.md
  echo "=== HEAD file bytes ==="
  git cat-file -s HEAD:query-kotobase.md 2>&1
  git show HEAD:query-cosientist.md 2>/dev/null > /tmp/kb_head_file.md
  wc -c /tmp/kb_head_file.md
  echo "=== working diff stat ==="
  git diff --stat query-cosientist.md
  echo "=== working file line29x tail ==="
  tail -c 500 query-cosientist.md
  echo ""
  echo "=== HEAD file tail ==="
  tail -c 500 /tmp/kb_head_file.md
} > "$OUT" 2>&1
echo done
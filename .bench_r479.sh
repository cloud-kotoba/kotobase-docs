#!/bin/bash
DOC=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md
OUT=/tmp/kb_r479.txt
{
  echo "=== run479 usage in doc ==="
  grep -n "run479" "$DOC"
  echo "=== run480 usage ==="
  grep -n "run480" "$DOC"
  echo "=== 16時台 mentions (recent) ==="
  grep -n "16時台" "$DOC" | tail -5
  echo "=== last 200 chars of doc ==="
  tail -c 200 "$DOC"
} > "$OUT" 2>&1
echo done
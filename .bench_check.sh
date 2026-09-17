#!/bin/bash
DOC=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md
OUT=/tmp/kb_check.txt
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== git status short ===" > "$OUT"
git status --short >> "$OUT" 2>&1
echo "=== run477 in file ===" >> "$OUT"
grep -c "run477" "$DOC" >> "$OUT" 2>&1
echo "=== run475 ===" >> "$OUT"
grep -c "run475" "$DOC" >> "$OUT" 2>&1
echo "=== last 100 chars of file ===" >> "$OUT"
tail -c 400 "$DOC" >> "$OUT" 2>&1
echo "" >> "$OUT"
echo "=== HEAD vs worktree diff stat ===" >> "$OUT"
git diff HEAD --stat >> "$OUT" 2>&1
echo "done"
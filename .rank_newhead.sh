#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank_newhead.out
: > "$OUT"
echo "===LOG===" >> "$OUT"; git log --oneline -5 >> "$OUT" 2>&1
echo "===STATUS===" >> "$OUT"; git status --short -- query-cosientist.md >> "$OUT" 2>&1
echo "===FULL-STATUS===" >> "$OUT"; git status --short >> "$OUT" 2>&1
echo done
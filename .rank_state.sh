#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank_state.out
: > "$OUT"
echo "=== HEAD ===" >> "$OUT"; git rev-parse HEAD >> "$OUT" 2>&1
echo "=== LOG ===" >> "$OUT"; git log --oneline -6 >> "$OUT" 2>&1
echo "=== STATUS ===" >> "$OUT"; git status --short >> "$OUT" 2>&1
echo "=== DATE ===" >> "$OUT"; date >> "$OUT" 2>&1
echo "=== DIFF STAT ===" >> "$OUT"; git diff HEAD --stat -- query-cosientist.md >> "$OUT" 2>&1
echo "=== DONE ===" >> "$OUT"
echo ok
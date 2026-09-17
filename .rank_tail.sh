#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank_tail.out
: > "$OUT"
git diff HEAD --stat -- query-cosientist.md >> "$OUT" 2>&1
echo "===TAIL===" >> "$OUT"
tail -12 /tmp/rank_state.out >> "$OUT" 2>&1
echo "===WC===" >> "$OUT"
git status --short -- query-cosientist.md | wc -l >> "$OUT" 2>&1
echo "===BRANCH===" >> "$OUT"
git branch --show-current >> "$OUT" 2>&1
echo done
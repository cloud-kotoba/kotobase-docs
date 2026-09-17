#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank198_wt.out
: > "$OUT"
echo "===WORKTREE-DIFF===" >> "$OUT"; git diff HEAD -- query-cosientist.md >> "$OUT" 2>&1
echo "===STATUS===" >> "$OUT"; git status --short -- query-cosientist.md >> "$OUT" 2>&1
echo done
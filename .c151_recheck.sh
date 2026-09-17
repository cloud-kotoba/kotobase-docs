#!/bin/sh
OUT=.c151_recheck.txt
: > "$OUT"
echo "=== now ===" >> "$OUT"
date '+%Y-%m-%d %H:%M:%S %z' >> "$OUT"
echo "=== current HEAD ===" >> "$OUT"
git rev-parse HEAD >> "$OUT" 2>&1
git log --oneline -6 >> "$OUT" 2>&1
echo "=== fetch both remotes ===" >> "$OUT"
git fetch net-kotobase 2>>"$OUT" >> "$OUT"
echo "net-kotobase fetch rc=$?" >> "$OUT"
git fetch bench_fetch 2>>"$OUT" >> "$OUT"
echo "bench_fetch fetch rc=$?" >> "$OUT"
echo "=== remote refs after fetch ===" >> "$OUT"
git rev-parse net-kotobase/main >> "$OUT" 2>&1
git rev-parse bench_fetch/main >> "$OUT" 2>&1
echo "=== tracked changes to doc (M/A/D) in status ===" >> "$OUT"
git status --short -- query-cosientist.md >> "$OUT" 2>&1
echo "=== diff HEAD vs worktree doc: bytes ===" >> "$OUT"
git diff HEAD -- query-cosientist.md | wc -c >> "$OUT" 2>&1
echo "=== HEAD ancestry: does HEAD contain falsify-230 (run518 commit)? ===" >> "$OUT"
git log --oneline --all | grep -i 'falsify 230\|run518\|falsify.230' | head -10 >> "$OUT" 2>&1
echo "=== top 4 iter-log lines (from file) with run518 context ===" >> "$OUT"
grep -n 'falsify 第230回\|bench 第230\|cosientist 第15[01]' query-cosientist.md | head -6 >> "$OUT" 2>&1
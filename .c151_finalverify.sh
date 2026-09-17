#!/bin/sh
OUT=.c151_finalverify.txt
: > "$OUT"
echo "=== HEAD ===" >> "$OUT"
git rev-parse HEAD >> "$OUT" 2>&1
echo "=== remotes (net-kotobase/main, bench_fetch/main) ===" >> "$OUT"
git rev-parse net-kotobase/main >> "$OUT" 2>&1
git rev-parse bench_fetch/main >> "$OUT" 2>&1
echo "=== worktree doc clean vs HEAD? (bytes) ===" >> "$OUT"
git diff HEAD -- query-cosientist.md | wc -c >> "$OUT" 2>&1
echo "=== tracked modified (M/A/D) ===" >> "$OUT"
git status --short | grep -v '^??' >> "$OUT" 2>&1
echo "(end)" >> "$OUT"
echo "=== run519 committed benchmark numbers (from bench230 iter line 409) ===" >> "$OUT"
grep -o 'cold(>=0.5s)[^—]*-[^—]*1/60[^—]*' query-cosientist.md | head -1 >> "$OUT" 2>&1
echo "=== 0時台 band: run516/517/518/519 present ===" >> "$OUT"
for r in run516 run517 run518 run519; do printf "%s: " "$r"; grep -c "$r" query-cosientist.md; done >> "$OUT" 2>&1
echo "=== time ===" >> "$OUT"
date '+%Y-%m-%d %H:%M:%S %z' >> "$OUT"
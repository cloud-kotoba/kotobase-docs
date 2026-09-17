#!/bin/sh
OUT=.c151_r226.txt
: > "$OUT"
git fetch net-kotobase 2>>"$OUT" >> "$OUT"
echo "net-kotobase rc=$?" >> "$OUT"
git fetch bench_fetch 2>>"$OUT" >> "$OUT"
echo "bench_fetch rc=$?" >> "$OUT"
echo "=== current HEAD ===" >> "$OUT"
git rev-parse HEAD >> "$OUT" 2>&1
git log --oneline -8 >> "$OUT" 2>&1
echo "=== remote refs ===" >> "$OUT"
git rev-parse net-kotobase/main >> "$OUT" 2>&1
git rev-parse bench_fetch/main >> "$OUT" 2>&1
python3 .c151_r226_py.py
echo "=== run519 count in worktree doc ===" >> "$OUT"
grep -c 'run519' query-cosientist.md >> "$OUT" 2>&1
echo "=== run520 count in worktree doc ===" >> "$OUT"
grep -c 'run520' query-cosientist.md >> "$OUT" 2>&1
echo "=== is doc worktree-modified vs HEAD? bytes ===" >> "$OUT"
git diff HEAD -- query-cosientist.md | wc -c >> "$OUT" 2>&1
cat .c151_r226_py.txt >> "$OUT" 2>&1
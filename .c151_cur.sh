#!/bin/sh
OUT=.c151_cur.txt
: > "$OUT"
echo "=== HEAD ===" >> "$OUT"
git rev-parse HEAD >> "$OUT" 2>&1
git log --oneline -3 >> "$OUT" 2>&1
echo "=== remotes ===" >> "$OUT"
git rev-parse net-kotobase/main >> "$OUT" 2>&1
git rev-parse bench_fetch/main >> "$OUT" 2>&1
echo "=== status short (M/A/D only, filtered from scratch) ===" >> "$OUT"
git status --short | grep -v '^??' >> "$OUT" 2>&1
echo "(end M/A/D list)" >> "$OUT"
echo "=== doc diff vs HEAD bytes ===" >> "$OUT"
git diff HEAD -- query-cosientist.md | wc -c >> "$OUT" 2>&1
echo "=== run519 in worktree doc (line count) ===" >> "$OUT"
grep -c 'run519' query-cosientist.md >> "$OUT" 2>&1
echo "=== run520 in worktree doc (line count) ===" >> "$OUT"
grep -c 'run520' query-cosientist.md >> "$OUT" 2>&1
echo "=== bench 230 iter-log line (first 900) ===" >> "$OUT"
python3 .c151_b230_py.py >> "$OUT" 2>&1
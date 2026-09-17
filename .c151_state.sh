#!/bin/sh
# cosientist 第151回 state check — write everything to a file (terminal stdout empty)
OUT=.c151_state.txt
: > "$OUT"
echo "=== DATE ===" >> "$OUT"
date '+%Y-%m-%d %H:%M:%S %z (%Z)' >> "$OUT"
echo "=== UPTIME/LOAD ===" >> "$OUT"
uptime >> "$OUT"
echo "=== HEAD ===" >> "$OUT"
git rev-parse HEAD >> "$OUT" 2>&1
git log --oneline -5 >> "$OUT" 2>&1
echo "=== REMOTE refs (net-kotobase/main, bench_fetch/main) ===" >> "$OUT"
git rev-parse net-kotobase/main 2>>"$OUT" >> "$OUT"
git rev-parse bench_fetch/main 2>>"$OUT" >> "$OUT"
echo "=== detached? ===" >> "$OUT"
git symbolic-ref -q HEAD >> "$OUT" 2>&1; echo "symbolic_ref_rc=$?" >> "$OUT"
echo "=== worktree diff to HEAD (query-cosientist.md) ===" >> "$OUT"
if git diff HEAD -- query-cosientist.md | wc -l | grep -q '^0'; then echo "doc clean: yes" >> "$OUT"; else echo "doc clean: NO" >> "$OUT"; fi
echo "=== highest run5xx used in doc ===" >> "$OUT"
grep -o 'run5[0-9][0-9]' query-cosientist.md | sort -u | tail -20 >> "$OUT" 2>&1
echo "=== does run518 appear as MEASURED (not just NEXT reference)? ===" >> "$OUT"
grep -c 'run518' query-cosientist.md >> "$OUT" 2>&1
echo "=== remote URL ===" >> "$OUT"
git remote -v >> "$OUT" 2>&1
echo "=== branch list (local) ===" >> "$OUT"
git branch -a 2>>"$OUT" | head -30 >> "$OUT" 2>&1
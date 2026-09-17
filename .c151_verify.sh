#!/bin/sh
OUT=.c151_verify.txt
: > "$OUT"
echo "=== is query-cosientist.md tracked-modified vs index? ===" >> "$OUT"
git status --short -- query-cosientist.md >> "$OUT" 2>&1
echo "rc=$?" >> "$OUT"
echo "=== diff HEAD vs worktree for doc: byte count ===" >> "$OUT"
git diff HEAD -- query-cosientist.md | wc -c >> "$OUT" 2>&1
echo "=== diff HEAD vs index for doc: byte count ===" >> "$OUT"
git diff --cached HEAD -- query-cosientist.md | wc -c >> "$OUT" 2>&1
echo "=== run518 context lines ===" >> "$OUT"
grep -n 'run518' query-cosientist.md >> "$OUT" 2>&1
echo "=== run517 measured occurrence (to confirm 517 committed, 518 is NEXT-only) ===" >> "$OUT"
grep -c 'run517' query-cosientist.md >> "$OUT" 2>&1
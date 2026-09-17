#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/rank198_verify.out
: > "$OUT"
echo "===ENTRY-IN-HEAD-BLOB===" >> "$OUT"; git show HEAD:query-cosientist.md | grep -c 'rank 第198回' >> "$OUT" 2>&1
echo "===ENTRY-IN-bench-main===" >> "$OUT"; git show bench_fetch/main:query-cosientist.md | grep -c 'rank 第198回' >> "$OUT" 2>&1
echo "===ENTRY-IN-net-main===" >> "$OUT"; git show net-kotobase/main:query-cosientist.md | grep -c 'rank 第198回' >> "$OUT" 2>&1
echo "===HEADER===" >> "$OUT"; git show HEAD:query-cosientist.md | grep -c '^## Iteration log' >> "$OUT" 2>&1
echo "===ORDER-head3===" >> "$OUT"; git show HEAD:query-cosientist.md | grep -n '^## Iteration log' >> "$OUT" 2>&1
echo "===WORKTREE-DIFF===" >> "$OUT"; git diff HEAD --stat -- query-cosientist.md >> "$OUT" 2>&1
echo done
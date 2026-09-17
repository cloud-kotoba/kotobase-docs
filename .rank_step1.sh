#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=/tmp/rank_state1.txt
: > "$OUT"
printf 'HEAD: ' >> "$OUT"
git rev-parse HEAD >> "$OUT" 2>&1
git fetch bench_fetch >> "$OUT" 2>&1
printf 'BENCH_FETCH_MAIN: ' >> "$OUT"
git rev-parse bench_fetch/main >> "$OUT" 2>&1
printf 'NET_KOTOBASE: ' >> "$OUT"
git rev-parse net-kotobase/main >> "$OUT" 2>&1
printf '%s\n' '---STATUS---' >> "$OUT"
git status --short >> "$OUT" 2>&1
printf '%s\n' '---DIFF---' >> "$OUT"
git diff HEAD --stat -- query-cosientist.md >> "$OUT" 2>&1
printf '%s\n' '===END===' >> "$OUT"

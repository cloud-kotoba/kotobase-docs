#!/bin/bash
# K-Z3 測定法: same as all prior sets (bench run420 precedent)
#   endpoint: search.kotobase.net/search?q=test  (curl separate conn, cold>=0.5s TTFB)
#   n=20 per run, 3 runs (A/B/C) + landing control (kotobase.net/signup)
#   nearest-rank p50,  接続再利用なし (each curl new connection = cold)
#   secret 不含 — curl only, stats via python
set -u
SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
OUTDIR="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
cd "$OUTDIR"

for RUN in A B C; do
  OUT="$OUTDIR/.b421_run421_${RUN}.txt"
  : > "$OUT"
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w "%{http_code} %{time_total}\n" --max-time 30 "$SEARCH" >> "$OUT" 2>&1
  done
done

# landing control (n=20)
OUT="$OUTDIR/.b421_run421_land.txt"
: > "$OUT"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w "%{http_code} %{time_total}\n" --max-time 30 "$CONTROL" >> "$OUT" 2>&1
done
echo "runner done: $(date '+%H:%M:%S')" > "$OUTDIR/.b421_done.txt"
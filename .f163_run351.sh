#!/bin/bash
# K-Z3 13時台 band-first measurement run351A-C + control
# n=20 x3 + landing control, separate curl connections, cold>=0.5s
# Endpoint: search.kotobase.net/search?q=test  control: kotobase.net/signup
# secret 不含 — curl only; writes results to stdout (redirected by caller)

ENDPOINT="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"
OUT=$1   # output file path

run_series() {
  local label="$1"
  local url="$2"
  local outf="$3"
  : > "$outf"
  for i in $(seq 1 20); do
    # curl -s -o /dev/null -w '%{time_total}' gives total time in seconds
    t=$(curl -s -o /dev/null -w '%{time_total}' --max-time 30 "$url")
    echo "$label:$i:$t" >> "$outf"
  done
}

OUTDIR="$1"
mkdir -p "$OUTDIR"
run_series "A" "$ENDPOINT" "$OUTDIR/run351A.txt"
run_series "B" "$ENDPOINT" "$OUTDIR/run351B.txt"
run_series "C" "$ENDPOINT" "$OUTDIR/run351C.txt"
run_series "control" "$CONTROL" "$OUTDIR/run351control.txt"
echo "DONE"
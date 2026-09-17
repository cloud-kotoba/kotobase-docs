#!/bin/bash
# K-Z3 run454 measurement (10時台 n-add, 5th set on 9/8): 3 sets n=20 search + landing control n=20 signup
# Same method as run450/451/452/453: curl separate connection, cold>=0.5s TTFB, nearest-rank p50
# one HTTP request per iteration (contract n=20), raw captures "http_code time_starttransfer"
set -u
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
# live smoke first (SOUL step 4)
echo -n "smoke /: " > "$OUT/.b454_smoke.txt"
curl -sS -o /dev/null -w "%{http_code}\n" "https://kotobase.net/" >> "$OUT/.b454_smoke.txt" 2>/dev/null
echo -n "smoke /signup: " >> "$OUT/.b454_smoke.txt"
curl -sS -o /dev/null -w "%{http_code}\n" "https://kotobase.net/signup" >> "$OUT/.b454_smoke.txt" 2>/dev/null
T0=$(date +%s%N)
for s in A B C; do
  rm -f "$OUT/.b454_run454${s}.ttfb" "$OUT/.b454_run454${s}_raw.ttfb"
  for i in $(seq 1 20); do
    curl -sS -o /dev/null \
      -w "%{http_code} %{time_starttransfer}\n" \
      "https://search.kotobase.net/search?q=test" >> "$OUT/.b454_run454${s}_raw.ttfb" 2>/dev/null
  done
done
# landing control
rm -f "$OUT/.b454_landing.ttfb"
for i in $(seq 1 20); do
  curl -sS -o /dev/null \
    -w "%{http_code} %{time_starttransfer}\n" \
    "https://kotobase.net/signup" >> "$OUT/.b454_landing_raw.ttfb" 2>/dev/null
done
T1=$(date +%s%N)
echo "elapsed_ms=$(( (T1-T0)/1000000 ))" > "$OUT/.b454_elapsed.txt"
date '+%Y-%m-%d %H:%M:%S JST' > "$OUT/.b454_t0.txt"
uptime > "$OUT/.b454_uptime.txt" 2>/dev/null
echo done
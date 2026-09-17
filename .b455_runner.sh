#!/bin/bash
# K-Z3 run455 measurement (10時台 n-add, 6th set on 9/8): 3 sets n=20 search + landing control n=20 signup
# Same method as run450/451/452/453/454: curl separate connection, cold>=0.5s TTFB, nearest-rank p50
# one HTTP request per iteration (contract n=20), raw captures "http_code time_starttransfer"
set -u
OUT=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
# live smoke first (SOUL step 4)
echo -n "smoke /: " > "$OUT/.b455_smoke.txt"
curl -sS -o /dev/null -w "%{http_code}\n" "https://kotobase.net/" >> "$OUT/.b455_smoke.txt" 2>/dev/null
echo -n "smoke /signup: " >> "$OUT/.b455_smoke.txt"
curl -sS -o /dev/null -w "%{http_code}\n" "https://kotobase.net/signup" >> "$OUT/.b455_smoke.txt" 2>/dev/null
T0=$(date +%s%N)
for s in A B C; do
  echo -n > "$OUT/.b455_run455${s}_raw.ttfb"
  for i in $(seq 1 20); do
    curl -sS -o /dev/null \
      -w "%{http_code} %{time_starttransfer}\n" \
      "https://search.kotobase.net/search?q=test" >> "$OUT/.b455_run455${s}_raw.ttfb" 2>/dev/null
  done
done
# landing control
echo -n > "$OUT/.b455_landing_raw.ttfb"
for i in $(seq 1 20); do
  curl -sS -o /dev/null \
    -w "%{http_code} %{time_starttransfer}\n" \
    "https://kotobase.net/signup" >> "$OUT/.b455_landing_raw.ttfb" 2>/dev/null
done
T1=$(date +%s%N)
echo "elapsed_ms=$(( (T1-T0)/1000000 ))" > "$OUT/.b455_elapsed.txt"
date '+%Y-%m-%d %H:%M:%S JST' > "$OUT/.b455_t0.txt"
uptime > "$OUT/.b455_uptime.txt" 2>/dev/null
echo done
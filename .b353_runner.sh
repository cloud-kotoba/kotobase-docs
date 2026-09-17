#!/bin/bash
# K-Z3 run353 measurement - same method: n=20 x 3 + landing control
# separate-connect curl, cold = TTFB >= 0.5s
SEARCH="https://search.kotobase.net/search?q=test"
LAND="https://kotobase.net/signup"
OUT=/tmp/b353_out.txt
: > "$OUT"
measure() {
  local tag="$1" url="$2"
  local ttfb_file=$(mktemp)
  for i in $(seq 1 20); do
    # start time in ns
    local s=$(date +%s%N)
    local code=$(curl -s -o /dev/null -w "%{http_code}" --connect-timeout 5 --max-time 20 "$url" -A "bench-kotobase/1.0")
    local e=$(date +%s%N)
    local ms=$(( (e - s) / 1000000 ))
    local frac=$(( (e - s) % 1000000 ))
    printf "%d %d.%06d\n" "$code" "$ms" "$frac" >> "$ttfb_file"
  done
  echo "=== $tag ===" >> "$OUT"
  cat "$ttfb_file" >> "$OUT"
  rm -f "$ttfb_file"
}
echo "start $(date '+%H:%M:%S')" >> "$OUT"
measure "run353A search" "$SEARCH"
measure "run353B search" "$SEARCH"
measure "run353C search" "$SEARCH"
measure "run353_land control" "$LAND"
echo "end $(date '+%H:%M:%S')" >> "$OUT"
echo "DONE"
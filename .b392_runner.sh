#!/bin/bash
# bench 第175回: K-Z3 20時台帯初計測 run392A-C + landing control
# 同一測定法: n=20 sequential per run, 別接続 curl, TTFB capture, cold>=0.5s
SEARCH_URL="https://search.kotobase.net/search?q=test"
CONTROL_URL="https://kotobase.net/signup"
OUT_DIR="."
measure_run() {
  local label="$1"
  local url="$2"
  local n="$3"
  local out="${OUT_DIR}/.b392_${label}.txt"
  : > "$out"
  for i in $(seq 1 "$n"); do
    # time_starttransfer = TTFB; http_code = status
    curl -s -o /dev/null -w "%{time_starttransfer}\t%{http_code}\n" --max-time 15 "$url" >> "$out"
    # small gap to avoid burst concatenation artifacts (separate connections already enforced)
    sleep 0.1
  done
  echo "$label done: $(wc -l < "$out") samples" >> "${OUT_DIR}/.b392_progress.txt"
}
echo "start $(date '+%H:%M:%S')" >> "${OUT_DIR}/.b392_progress.txt"
measure_run "392A" "$SEARCH_URL" 20
measure_run "392B" "$SEARCH_URL" 20
measure_run "392C" "$SEARCH_URL" 20
measure_run "land" "$CONTROL_URL" 20
echo "finish $(date '+%H:%M:%S')" >> "${OUT_DIR}/.b392_progress.txt"
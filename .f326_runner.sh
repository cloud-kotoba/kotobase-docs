#!/bin/bash
# falsify run326A-C: K-Z3 7時台 n 積み増し
# Method: n=20 x 3 windows (A/B/C) + landing control, separate curl conn,
# cold>=0.5s time_starttransfer, nearest-rank p50. Endpoint search.kotobase.net/search?q=test.
# Output: one line per request.
RET_DIR=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
SEARCH="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"
log="$RET_DIR/.f326_out.txt"
: > "$log"

measure_window () {
  local label="$1"; local url="$2"
  echo "=== $label ===" >> "$log"
  for i in $(seq 1 20); do
    local t code
    tf=$(curl -s -o /dev/null -w '%{time_starttransfer} %{http_code}' --max-time 15 "$url")
    code="${tf##* }"
    t="${tf%% *}"
    echo "$i $t $code" >> "$log"
  done
}

measure_window "run326A" "$SEARCH"
measure_window "run326B" "$SEARCH"
measure_window "run326C" "$SEARCH"
measure_window "control-signup" "$CTRL"
echo "DONE" >> "$log"
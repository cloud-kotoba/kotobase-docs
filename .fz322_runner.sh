#!/bin/sh
# K-Z3 current-band(7時台) n-add run322A-C + landing control, production HTTP (gate-exempt)
# Method: n=20 x 3 runs + landing control, separate-connection curl, Tokyo,
# cold threshold time_total >= 0.5s. One request = one curl (fresh conn).
RAW=/tmp/fz322.raw
: > "$RAW"

SEARCH="https://search.kotobase.net/search?q=test"
CONTROL="https://kotobase.net/signup"

run_batch () {
  label="$1"; url="$2"
  i=1
  while [ "$i" -le 20 ]; do
    printf "%s %s " "$label" "$i" >> "$RAW"
    curl -s -o /dev/null -m 10 -w "%{time_total} %{http_code}\n" "$url" >> "$RAW"
    sleep 0.1
    i=$((i+1))
  done
}

run_batch A "$SEARCH"
run_batch B "$SEARCH"
run_batch C "$SEARCH"
run_batch CTRL "$CONTROL"

echo "DONE"
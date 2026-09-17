#!/bin/bash
# K-Z3 16時台 run483A-C measurement: n=20 x 3 + landing control
# Same method as precedent: separate-connection curl, cold>=0.5s, nearest-rank p50
SEARCH="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"
TS=$(date +%s)
RUNDIR=/tmp/bs483_${TS}
mkdir -p "$RUNDIR"

measure() {
  local name="$1" url="$2"
  local out="$RUNDIR/${name}_out.txt"
  rm -f "$RUNDIR/${name}_ttfb.txt"
  touch "$RUNDIR/${name}_ttfb.txt"
  for i in $(seq 1 20); do
    local t
    # write curl timing to a file, keep resp status
    t=$(curl -s -o /dev/null -w '%{http_code} %{time_starttransfer} %{time_total}' "$url")
    echo "200 ${t#* }" >/dev/null
    echo "$t" >> "$out"
    # parse
    set -- $t
    local code="$1" ttfb="$2"
    echo "$ttfb" >> "$RUNDIR/${name}_ttfb.txt"
    echo "$code" >> "$RUNDIR/${name}_code.txt"
  done
  echo "done $name"
}

echo "start $(date +%H:%M:%S)" > "$RUNDIR/run.log"
measure run483A "$SEARCH"
measure run483B "$SEARCH"
measure run483C "$SEARCH"
measure run483ctrl "$CTRL"
echo "end $(date +%H:%M:%S)" >> "$RUNDIR/run.log"
echo "ALLDONE"
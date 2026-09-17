#!/bin/sh
# bench K-Z3 6時台(深夜帯→朝の帯境) n-add run318A-C + landing control, same method:
# n=20 x 3 search + landing control, separate-connection curl (fresh conn each), Tokyo,
# cold threshold time_total >= 0.5s. production HTTP, gate-exempt.
RAW=/tmp/bench318.raw
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

date '+start %Y-%m-%dT%H:%M:%S%z' > /tmp/bench318_time.txt
run_batch A "$SEARCH"
run_batch B "$SEARCH"
run_batch C "$SEARCH"
run_batch CTRL "$CONTROL"
date '+end %Y-%m-%dT%H:%M:%S%z' >> /tmp/bench318_time.txt
uptime >> /tmp/bench318_time.txt
echo "DONE"
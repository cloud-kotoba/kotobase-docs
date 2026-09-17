#!/bin/sh
# K-Z3 19時台 n 積み増し run584A-C + landing control (falsify担当, cron tick)
D=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
B=$D/.b584
mkdir -p "$B"
date '+%H:%M:%S start' >> "$B/meta.txt"

seq_loop() {
  label=$1
  url=$2
  n=0
  while [ $n -lt 20 ]; do
    n=$((n+1))
    curl -s -o /dev/null --connect-timeout 10 -m 20 -w '%{time_total}\n' "$url" >> "$B/$label.txt"
  done
}

seq_loop run584A 'https://search.kotobase.net/search?q=test'
date '+%H:%M:%S A done' >> "$B/meta.txt"
seq_loop run584B 'https://search.kotobase.net/search?q=test'
date '+%H:%M:%S B done' >> "$B/meta.txt"
seq_loop run584C 'https://search.kotobase.net/search?q=test'
date '+%H:%M:%S C done' >> "$B/meta.txt"
seq_loop control 'https://kotobase.net/signup'
date '+%H:%M:%S control done' >> "$B/meta.txt"
uptime >> "$B/meta.txt"
wc -l "$B"/*.txt >> "$B/meta.txt"

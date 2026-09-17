#!/bin/bash
# cosientist 2026-09-10 K-Z3 1時台 n 積み増し run575A-C (fallback: current-band)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
U='https://search.kotobase.net/search?q=test'
C='https://kotobase.net/signup'
date '+%Y-%m-%d %H:%M:%S %Z' > .c152_t0.txt
uptime >> .c152_t0.txt
for s in A B C; do
  f=.c152_run575_${s}.ttfb
  : > "$f"
  i=1
  while [ $i -le 20 ]; do
    curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --max-time 15 "$U" >> "$f"
    i=$((i+1))
  done
done
: > .c152_run575_landing.ttfb
i=1
while [ $i -le 20 ]; do
  curl -s -o /dev/null -w '%{http_code} %{time_starttransfer}\n' --max-time 15 "$C" >> .c152_run575_landing.ttfb
  i=$((i+1))
done
date '+%Y-%m-%d %H:%M:%S %Z' >> .c152_t0.txt
uptime >> .c152_t0.txt

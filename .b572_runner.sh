#!/bin/bash
# K-Z3 15hr-band first run572A-C + landing control
# same method: n=20 x 3 + control, separate-connection curl, cold >= 0.5s
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for s in A B C; do
  : > .b572_${s}.ttfb
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w '%{time_starttransfer}\n' --max-time 10 'https://search.kotobase.net/search?q=test' >> .b572_${s}.ttfb
  done
done
: > .b572_ctl.ttfb
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --max-time 10 'https://kotobase.net/signup' >> .b572_ctl.ttfb
done
date '+%H:%M:%S' > .b572_done.txt

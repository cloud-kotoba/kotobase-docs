#!/bin/bash
# K-Z3 13hr-band n-add run571A-C + landing control
# same method: n=20 x 3 + control, separate-connection curl, cold >= 0.5s
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for s in A B C; do
  : > .b571_${s}.ttfb
  for i in $(seq 1 20); do
    curl -s -o /dev/null -w '%{time_starttransfer}\n' --max-time 10 'https://search.kotobase.net/search?q=test' >> .b571_${s}.ttfb
  done
done
: > .b571_ctl.ttfb
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --max-time 10 'https://kotobase.net/signup' >> .b571_ctl.ttfb
done
date '+%H:%M:%S' > .b571_done.txt

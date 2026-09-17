#!/bin/sh
# K-Z3 11h-band (9/11) n-topup run579A-C + landing control. Separate curl connections, Tokyo.
# Each set: 20 sequential requests to https://kotobase.net/api/search?q=... with fresh connection.
# Cold = >=0.5s. Output raw ttfb lines to files.
for S in A B C; do
  : > .b579_run$S.txttfb
  i=0
  while [ $i -lt 20 ]; do
    i=$((i+1))
    T=$(curl -sS -o /dev/null -w '%{time_starttransfer}' --max-time 10 "https://kotobase.net/api/search?q=%E7%8A%AC&limit=5") || T=ERR
    printf '%s\n' "$T" >> .b579_run$S.txttfb
  done
done
: > .b579_control.txttfb
i=0
while [ $i -lt 20 ]; do
  i=$((i+1))
  T=$(curl -sS -o /dev/null -w '%{time_starttransfer}' --max-time 10 "https://kotobase.net/signup") || T=ERR
  printf '%s\n' "$T" >> .b579_control.txttfb
done
date -u +%FT%TZ >> .b579_landing.txt

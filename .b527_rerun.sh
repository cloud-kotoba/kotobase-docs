#!/bin/bash
# Re-run B + landing for run527
OUT=".b527_run527"
SEARCH="https://search.kotobase.net/search?q=test"
LANDING="https://kotobase.net/signup"
MT="--max-time"
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 $MT 20 "$SEARCH" >> "${OUT}_B.ttfb" 2>/tmp/b527_curl_B.err
done
for i in $(seq 1 20); do
  curl -s -o /dev/null -w '%{time_starttransfer}\n' --connect-timeout 10 $MT 20 "$LANDING" >> "${OUT}_landing.ttfb" 2>/tmp/b527_curl_L.err
done
echo "rerun_B_L done"
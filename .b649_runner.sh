#!/bin/sh
# falsify run649: K-Z3 3時台 cold-rate n 積み増し (A/B/C 20x3 + landing control)
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
EP_PROBE=0
for EP in "https://search.kotobase.net/search?q=test" "https://search.yataverse.com/search?q=test"; do
  code=$(curl -s -o .b649_probe_body.txt -w '%{http_code}' "$EP")
  echo "$EP -> $code" > .b649_probe.txt
  if [ "$code" = "200" ]; then EP_PROBE=1; SELECTED_EP="$EP"; break; fi
done
echo "selected: $SELECTED_EP" >> .b649_probe.txt
if [ "$EP_PROBE" != "1" ]; then echo "NO_ENDPOINT_200" >> .b649_probe.txt; exit 3; fi

EP="$SELECTED_EP"
date '+%s start %H:%M:%S' > .b649_times.txt
for s in A B C; do
  n=0
  while [ $n -lt 20 ]; do
    t0=$(python3 -c 'import time; print(time.time())')
    code=$(curl -s --no-keepalive -o /dev/null -w '%{http_code}' "$EP")
    t1=$(python3 -c 'import time; print(time.time())')
    echo "$s $n $code $(python3 -c "print(round($t1-$t0,3))")" >> .b649_samples.txt
    n=$((n+1))
  done
done
n=0
while [ $n -lt 20 ]; do
  t0=$(python3 -c 'import time; print(time.time())')
  code=$(curl -s --no-keepalive -o /dev/null -w '%{http_code}' "https://kotoba.cloud/")
  t1=$(python3 -c 'import time; print(time.time())')
  echo "L $n $code $(python3 -c "print(round($t1-$t0,3))")" >> .b649_samples.txt
  n=$((n+1))
done
date '+%s end %H:%M:%S' >> .b649_times.txt

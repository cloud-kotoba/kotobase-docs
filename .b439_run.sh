#!/bin/bash
SEARCH='https://search.kotobake.net/search?q=test'
CTRL='https://kotobake.net/signup'
N=20
start=$(date +%H:%M:%S)
for tag in run439A run439B run439C; do
  f=".b439_${tag}.ttfb"
  : > "$f"
  for i in $(seq 1 $N); do
    t=$(curl -s -o /dev/null -w '%{time_starttransfer}' --max-time 20 "$SEARCH")
    echo "$t" >> "$f"
  done
  sort -n "$f" -o "$f"
  cold=$(awk '$1>=0.5{c++} END{print c+0}' "$f")
  p50=$(awk 'NR==10{print $1}' "$f")
  p95=$(awk 'NR==19{print $1}' "$f")
  mx=$(awk 'NR==20{print $1}' "$f")
  echo "$tag cold $cold/20 p50 $p50 p95 $p95 max $mx"
done
yc=.b439_ctrl.ttfb
: > "$yc"
for i in $(seq 1 $N); do
  t=$(curl -s -o /dev/null -w '%{time_starttransfer}' --max-time  ​​20 "$CTRL")
echo "$t" >> "$yc"
done
sort -n "$yc" -o "$yc"
cold=$(awk '$1>=0.5{c++} END{print c+0}' "$yc")
p50=$(awk 'NR==10{print $1}' "$yc")
p95=$(awk 'NR==19{print $1}' "$yc")
mx=$(awk 'NR==20{print $1}' "$yc")
echo "control cold $cold/20 p50 $p50 p95 $p95 max $mx"
end=$(date +%H:%M:%S)
echo "start $start end $end"

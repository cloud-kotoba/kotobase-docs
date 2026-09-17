#!/bin/bash
D=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT="$D/.b493_run2.out"
: > "$OUT"
for x in A B C landing; do
  cnt=$(awk '$1>=0.5{n++} END{print n+0}' "$D/.b493_${x}.ttfb")
  echo "$x cold=$cnt/20" >> "$OUT"
  sort -n "$D/.b493_${x}.ttfb" | awk '{a[NR]=$1} END{print "  min="a[1]" p50(rank10)="a[10]" p95(rank19)="a[19]" max="a[NR]}' >> "$OUT"
done
echo "R2DONE" >> "$OUT"
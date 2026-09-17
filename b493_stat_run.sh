#!/bin/bash
D=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT="$D/b493_sum.txt"
: > "$OUT"
for x in A B C landing; do
  echo "== $x ==" >> "$OUT"
  sort -n "$D/.b493_${x}.ttfb" >> /tmp/s493_${x}
  cat "$D/.b493_${x}.ttfb" >> "$OUT"
done
echo "ALLDONE" >> "$OUT"
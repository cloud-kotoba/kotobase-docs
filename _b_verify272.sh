#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
for f in _b_run272A.txt _b_run272B.txt _b_run272C.txt _b_land272.txt; do
  lc=$(wc -l < "$f")
  n200=$(grep -c '^200 ' "$f")
  echo "$f: lines=$lc status200=$n200"
done
echo "--- header of A ---"
head -3 _b_run272A.txt
echo "--- header of B ---"
head -3 _b_run272B.txt
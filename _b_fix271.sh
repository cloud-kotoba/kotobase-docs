#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== run271A occurrences in whole file ==="
grep -oF 'run271A' query-cosientist.md | wc -l
echo "=== run271 in K-Z3 row line 260 ==="
awk 'NR==260' query-cosientist.md | grep -oF 'run271' | wc -l
echo "=== last 2000 chars of K-Z3 row line 260 ==="
awk 'NR==260' query-cosientist.md | tail -c 2000
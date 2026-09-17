#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== count run271 in K-Z3 row ==="
awk 'NR==260' query-cosientist.md | grep -o 'run271' | wc -l
echo "=== tail -c 1500 of K-Z3 row ==="
awk 'NR==260' query-cosientist.md | tail -c 1500
#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== lines containing run271A ==="
grep -nF 'run271A' query-cosientist.md | cut -c1-60
echo "=== does K-Z3 row (line 260) contain run270/run269? ==="
awk 'NR==260' query-cosientist.md | grep -oF 'run270' | wc -l
awk 'NR==260' query-cosientist.md | grep -oF 'run269' | wc -l
awk 'NR==260' query-cosientist.md | grep -oF 'run272' | wc -l
echo "=== total lines ==="
wc -l query-cosientist.md
echo "=== last char of line 260 ==="
awk 'NR==260' query-cosientist.md | tail -c 3 | od -c | head -2
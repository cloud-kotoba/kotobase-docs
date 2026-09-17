#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== line 259 ==="
sed -n '259p' query-cosientist.md | cut -c1-80
echo "=== line 260 length ==="
awk 'NR==260 {print length($0)}' query-cosientist.md
echo "=== line 261-266 ==="
sed -n '261,267p' query-cosientist.md | cut -c1-80
echo "=== does K-Z3 row contain 'bench 2026-09-07' or 'falsify 2026-09-07'? ==="
awk 'NR==260' query-cosientist.md | grep -oF 'bench 2026-09-07' | wc -l
awk 'NR==260' query-cosientist.md | grep -oF 'falsify 2026-09-07' | wc -l
echo "=== what's at line 260 col about run269? search show line 260 for run26x ==="
awk 'NR==260' query-cosientist.md | grep -oF 'run26[0-9]' | sort | uniq -c
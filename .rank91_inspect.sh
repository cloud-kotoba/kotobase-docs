#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== Iteration log header line ==="
grep -n 'Iteration log' query-cosientist.md | head -5
echo "=== all rank NNN回 occurrences (full) ==="
grep -oE 'rank 第[0-9]+回' query-cosientist.md | sort -V | uniq | tail -20
echo "=== all 'rank 第1' 3-digit ==="
grep -oE 'rank 第1[0-9][0-9]回' query-cosientist.md | sort -V | uniq | tail -20
echo "=== latest 4 lines of file ==="
tail -4 query-cosientist.md
echo "=== search for 'NEXT:' line count ==="
grep -c 'NEXT' query-cosientist.md
echo "=== END ==="
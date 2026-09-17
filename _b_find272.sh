#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== highest bench iter in iter log ==="
grep -oE 'bench 第[0-9]+回' query-cosientist.md | sort -t'第' -k2 -n | tail -3
echo "=== K-Z3 row line range ==="
grep -n '^| K-Z3 ' query-cosientist.md
echo "=== latest iterlog entry (first line) ==="
sed -n '316,317p' query-cosientist.md | cut -c1-120
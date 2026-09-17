#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== header count ==="
grep -c "^## Iteration log" query-cosientist.md
echo "=== first lines after header ==="
awk 'NR>=365 && NR<=369' query-cosientist.md | cut -c1-120
echo "=== entry present? ==="
grep -c "rank  第163回" query-cosientist.md
echo "=== git status md ==="
git status --short query-cosientist.md
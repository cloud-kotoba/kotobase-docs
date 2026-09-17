#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== lines 266-272 (head 60 chars each) ==="
sed -n '266,272p' query-cosientist.md | awk '{print NR": "$0}' | cut -c1-70
echo ""
echo "=== last physical line of K-Z3 row: find the line ending with the row terminator ==="
awk 'NR>=259 && NR<=272 && $0 ~ /\| K-Z2 |/ {print "row-end at line " NR}' query-cosientist.md
grep -nF '| K-Z2 | worker' query-cosientist.md | cut -c1-40
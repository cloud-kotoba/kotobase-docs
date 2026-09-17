#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== last 600 chars of K-Z3 row (line 260) ==="
awk 'NR==260' query-cosientist.md | tail -c 700
echo ""
echo "=== SPLIT marker ==="
echo "=== first 2 lines of iterlog ==="
sed -n '316,317p' query-cosientist.md
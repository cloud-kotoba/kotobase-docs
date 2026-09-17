#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== line 268 last 120 chars (run271 entry end) ==="
sed -n '268p' query-cosientist.md | tail -c 120
echo ""
echo "=== line 269 first 50 chars ==="
sed -n '269p' query-cosientist.md | cut -c1-50
echo ""
echo "=== confirm line 268 contains 'run271A-C' (run271 entry) ==="
sed -n '268p' query-cosientist.md | grep -oF 'run271A-C' | head -1
sed -n '268p' query-cosientist.md | grep -oF '第124回' | head -1
echo ""
echo "=== line count sanity: is line 269 a new evidence line or row? line13-15 check ==="
sed -n '313,315p' query-cosientist.md | cut -c1-40
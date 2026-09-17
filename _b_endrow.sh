#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== line 268 full (run271 entry) last 400 chars ==="
sed -n '268p' query-cosientist.md | tail -c 400
echo ""
echo "=== line 269 (should be K-Z3 next?) ==="
sed -n '269p' query-cosientist.md | cut -c1-60
echo ""
echo "=== find next data-row header after line 268 ==="
grep -nE '^\| K-S[0-9] |^\| K-Z[0-9] ' query-cosientist.md
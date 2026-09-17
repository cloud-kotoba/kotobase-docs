#!/bin/bash
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
OUT=/tmp/cos_write2.txt
{
echo "=== find proxy.cljc ==="
find "$CP" -name 'proxy.cljc' -not -path '*/target/*' 2>/dev/null
echo "=== find bind-tenant-write-graph ==="
grep -rln 'bind-tenant-write-graph' "$CP" --include='*.clj' --include='*.cljs' --include='*.cljc' 2>/dev/null | grep -v target | head
echo "=== harness transact block (lines 245-290) ==="
sed -n '245,290p' "$CP/authn/scripts/live_biscuit_query_bench.mjs" 2>/dev/null
echo "=== harness header setup (lines 80-120) ==="
sed -n '80,120p' "$CP/authn/scripts/live_biscuit_query_bench.mjs" 2>/dev/null
echo "=== END ==="
} > "$OUT" 2>&1
echo "rc=$?" >> "$OUT"
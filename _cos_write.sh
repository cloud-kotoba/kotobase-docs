#!/bin/bash
# Inspect bind-tenant-write-graph CACAO path + existing write harness shape.
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
W="$CP/kotobase-api-gateway-cljs/src/kotobase/kotobase_api_gateway_cljs/proxy.cljc"
OUT=/tmp/cos_write.txt
{
echo "=== proxy.cljc bind-tenant-write-graph / CACAO region (930-1000) ==="
sed -n '930,1000p' "$W" 2>&1
echo "=== cacao_b64 usages in proxy.cljc ==="
grep -n 'cacao_b64\|cacao' "$W" 2>&1 | head -30
echo "=== live_biscuit_query_bench.mjs: transact section ==="
grep -n 'transact\|cacao\|db_name\|tx_edn\|provision\|/api/transact' "$CP/authn/scripts/live_biscuit_query_bench.mjs" 2>&1 | head -40
echo "=== END ==="
} > "$OUT" 2>&1
echo "rc=$?" >> "$OUT"
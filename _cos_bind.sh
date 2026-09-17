#!/bin/bash
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
P="$CP/kotobase-api-gateway-cljs/src/kotobase/proxy.cljc"
OUT=/tmp/cos_bind.txt
{
echo "=== bind-tenant-write-graph region (search line nos) ==="
grep -n 'bind-tenant-write-graph\|cacao_b64\|CACAO\|x-kotobase-cacao\|authorize-tenant-cap-write' "$P" 2>&1 | head -40
echo "=== END ==="
} > "$OUT" 2>&1
echo "rc=$?" >> "$OUT"
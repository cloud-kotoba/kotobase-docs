#!/bin/bash
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
P="$CP/kotobase-api-gateway-cljs/src/kotobase/proxy.cljc"
OUT=/tmp/cos_bind2.txt
{
echo "=== proxy.cljc lines 958-1030 ==="
sed -n '958,1030p' "$P" 2>&1
echo "=== END ==="
} > "$OUT" 2>&1
echo "rc=$?" >> "$OUT"
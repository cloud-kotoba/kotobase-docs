#!/bin/bash
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
{
echo "=== harness file ==="
find "$CP" -name 'live_biscuit_query_bench.mjs' 2>/dev/null
echo "=== cacao_b64 references ==="
grep -rn 'cacao_b64' "$CP" --include='*.mjs' --include='*.clj' --include='*.cljs' --include='*.js' 2>/dev/null | head -40
echo "=== authn scripts dir ==="
ls -la "$CP/authn/scripts/" 2>&1 | head -40
} > /tmp/cos_harness.txt 2>&1
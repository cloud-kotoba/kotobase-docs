#!/bin/bash
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
E=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine
{
echo "=== cacao module files ==="
find "$CP/migrations/cljc-worker-v2-v3/src/kotobase" -iname '*cacao*' 2>/dev/null
echo "=== engine mint-cacao.mjs ==="
sed -n '1,80p' "$E/test/mint-cacao.mjs" 2>/dev/null
echo "=== authn cacao mint in control-plane (cljs source, not target) ==="
grep -rln 'mint-cacao\|mint_cacao\|defn mint' "$CP" --include='*.cljs' --include='*.clj' 2>/dev/null | grep -v target | head
} > /tmp/cos_cacao.txt 2>&1
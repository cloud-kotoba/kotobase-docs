#!/bin/bash
# cosientist recon: locate cacao mint capability for K-Q1 cut(ii) harness change.
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
E=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine
OUT=/tmp/recon3.txt
{
echo "=== repos exist? ==="
ls -d "$CP" "$E" 2>&1
echo "=== harness: live_biscuit_query_bench.mjs ==="
find "$CP" -name 'live_biscuit_query_bench.mjs' 2>/dev/null | head
echo "=== harness: *kq1*.mjs ==="
find "$CP" -name '*kq1*.mjs' 2>/dev/null | head
echo "=== harness: *tx401* / cosient* ==="
find "$CP" -name '*tx401*' -o -name '_cosient7*mjs' 2>/dev/null | head
echo "=== engine mint-cacao.mjs ==="
ls -la "$E/test/mint-cacao.mjs" 2>&1
echo "=== cacao_b64 refs (source, no target) ==="
grep -rln 'cacao_b64' "$CP" --include='*.clj' --include='*.cljs' --include='*.mjs' 2>/dev/null | grep -v target | head
echo "=== END ==="
} > "$OUT" 2>&1
echo "rc=$?" >> "$OUT"
#!/bin/bash
CP=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane
E=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine
{
echo "=== mint.cljs ==="
sed -n '1,60p' "$CP/migrations/cljc-worker-v2-v3/src/kotobase/cljc_worker/mint.cljs" 2>/dev/null
echo "=== engine pack tests ==="
grep -rln 'KOTOBASE_PACK_WRITES\|pack-writes\|packWrite\|:pack' "$E/test" "$E/src" 2>/dev/null | head -20
echo "=== engine test files (local) ==="
ls "$E/test" 2>/dev/null
} > /tmp/cos_mint.txt 2>&1
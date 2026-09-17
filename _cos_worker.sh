#!/bin/bash
W=/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/migrations/cljc-worker-v2-v3/src/kotobase/cljc_worker/worker.cljs
{
echo "=== transact dispatch / datomic.transact handler ==="
grep -n 'transact\|datomic.transact\|:db_name\|tx_edn\|authorize-tenant-cap-write\|write-delegation\|delegation' "$W" | head -80
} > /tmp/cos_worker.txt 2>&1
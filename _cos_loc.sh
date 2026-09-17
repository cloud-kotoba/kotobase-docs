#!/bin/bash
{
echo "=== orgs tree (top) ==="
ls -d /Users/junkawasaki/github/com-junkawasaki/orgs/*/ 2>&1
echo "=== net-kotobase tree ==="
ls -d /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/*/ 2>&1
echo "=== find harness ==="
find /Users/junkawasaki/github -name 'live_biscuit_query_bench.mjs' 2>/dev/null | head
echo "=== find cacao_b64 refs ==="
grep -rl 'cacao_b64' /Users/junkawasaki/github/com-junkawasaki/orgs 2>/dev/null | head
} > /tmp/cos_loc.txt 2>&1
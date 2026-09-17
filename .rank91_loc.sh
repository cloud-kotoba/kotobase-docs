#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== line numbers of rank 第113/114/115回 ==="
grep -n 'rank 第11[345]回' query-cosientist.md
echo "=== line numbers of bench 107 / cosientist 116 / run264 / run265 ==="
grep -n 'run264\|run265\|bench 107\|cosientist 116' query-cosientist.md | head -20
echo "=== total lines ==="
wc -l query-cosientist.md
echo "=== first 6 rank entries after header (chronological start of log) ==="
sed -n '311,389p' query-cosientist.md | grep -nE 'rank 第|falsify 第|bench 第|cosientist 第' | head -30
echo "=== END ==="
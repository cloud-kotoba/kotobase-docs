#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== grep run440 ==="
grep -n "run440" query-cosientist.md | head -20
echo "=== grep run441 ==="
grep -n "run441" query-cosientist.md | head -20
echo "=== grep rank 第195/194th/第194 ==="
grep -n "rank 第19[4-5]\|rank 194\|rank 195\|rank 第194\|rank 第195" query-cosientist.md | head -20
echo "=== grep bench 第195 ==="
grep -n "bench 第195\|bench 195th" query-cosientist.md | head
echo "=== grep falsify 第195 ==="
grep -n "falsify 第195\|falsify 195th" query-cosientist.md | head
echo "=== grep HEAD refs / latest entries ==="
grep -n "ade7b72\|08e1e42\|25a9492" query-cosientist.md | head
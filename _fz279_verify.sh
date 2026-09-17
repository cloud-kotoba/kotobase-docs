#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== run279 occurrence count ==="
grep -c "run279" query-cosientist.md
echo "=== run279A measurement occurrences (should be 1) ==="
grep -c "run279A" query-cosientist.md
echo "=== runt278 occurrence count now should still be 2 ==="
grep -c "run278" query-cosientist.md
echo "=== inserted line ==="
grep -n "第127回, K-Z3 1時台 n 積み増し run279" query-cosientist.md | head -2
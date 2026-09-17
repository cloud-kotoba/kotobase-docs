#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase 2>&1
echo "=== HEAD ==="
git rev-parse HEAD
echo "=== remote main ==="
git rev-parse net-kotobase/main 2>&1
echo "=== run279 measurement refs (not NEXT mentions) ==="
grep -n "run279A" query-cosientist.md | head -5
echo "=== current count run279 ==="
grep -c "run279" query-cosientist.md
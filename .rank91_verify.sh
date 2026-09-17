#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD commit ==="
git log -1 --format='%H %s' 2>&1
echo "=== working tree file line count ==="
wc -l query-cosientist.md 2>&1
echo "=== HEAD blob line count ==="
git show HEAD:query-cosientist.md 2>&1 | wc -l
echo "=== last 'rank 第' occurrences in HEAD blob ==="
git show HEAD:query-cosientist.md 2>&1 | grep -oE 'rank 第[0-9]+回' | sort -u | tail -8
echo "=== last 'rank 第' occurrences in working tree ==="
grep -oE 'rank 第[0-9]+回' query-cosientist.md | sort -u | tail -8
echo "=== END ==="
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD blob header count ==="
git show HEAD:query-cosientist.md | grep -c "^## Iteration log"
echo "=== entry present in HEAD blob ==="
git show HEAD:query-cosientist.md | grep -c "rank  第163回"
echo "=== entry order (first 4 iter lines) ==="
git show HEAD:query-cosientist.md | grep -n "^## Iteration log" | head -1
git show HEAD:query-cosientist.md | sed -n 's/^## Iteration log$//p' | head -4 | cut -c1-110
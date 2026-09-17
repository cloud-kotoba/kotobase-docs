#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD md iteration log tail (last 30 lines) ==="
git show HEAD:query-cosientist.md 2>&1 | tail -30
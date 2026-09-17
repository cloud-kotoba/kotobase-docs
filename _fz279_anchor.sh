#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
grep -n "第113回, K-Z3 1時台" query-cosientist.md | head -3
echo "---"
grep -c "run278" query-cosientist.md
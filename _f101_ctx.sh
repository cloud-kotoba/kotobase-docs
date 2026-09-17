#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase
echo "FETCH_EXIT=$?"
echo "HEAD=$(git rev-parse HEAD)"
echo "MAIN=$(git rev-parse net-kotobase/main)"
echo "---section headers near evidence block---"
grep -n "^##\|^###\|^####" query-cosientist.md | tail -20
echo "---lines 265-276---"
sed -n '265,276p' query-cosientist.md
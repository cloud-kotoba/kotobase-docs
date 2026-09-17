#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "---grep 第101回---"
grep -c "第101回" query-cosientist.md
echo "---grep run232---"
grep -c "run232" query-cosientist.md
echo "---context around insertion (evidence block tail)---"
grep -n "第101回" query-cosientist.md | head
echo "---git diff stat---"
git diff --stat
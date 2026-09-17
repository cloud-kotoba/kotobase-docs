#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
git fetch origin 2>&1
echo "---"
git branch -r --contains HEAD 2>/dev/null | sed -n '1,5p'
echo "--- remote tip:"
git log --oneline -1 origin/main 2>&1
echo "--- HEAD:"
git log --oneline -1 HEAD
echo "--- load:"
uptime
echo "--- grep NEXT/quiet in doc:"
grep -n "quiet-host" query-cosientist.md | tail -5

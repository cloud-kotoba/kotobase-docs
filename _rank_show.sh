#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git show --stat HEAD > /tmp/rank_show.txt 2>&1
echo "=== DIFF (added lines matching run236) ===" >> /tmp/rank_show.txt
git show HEAD -- query-cosientist.md | grep -E '^\+' >> /tmp/rank_show.txt 2>&1
echo "DONE" >> /tmp/rank_show.txt
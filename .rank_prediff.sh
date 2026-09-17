#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git diff HEAD --stat -- query-cosientist.md > .rank_prediff.txt 2>&1
echo "diffexit:$?" >> .rank_prediff.txt
wc -c < .rank_prediff.txt >> .rank_prediff.txt
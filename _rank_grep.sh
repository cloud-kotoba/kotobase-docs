#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
echo "==== run236 contexts ====" >> /tmp/rank_g.txt
grep -n "run236" query-cosientist.md >> /tmp/rank_g.txt 2>&1
echo "==== 19時台 карти ====" >> /tmp/rank_g.txt
grep -n "19時台通算" query-cosientist.md >> /tmp/rank_g.txt 2>&1
echo "==== line count ====" >> /tmp/rank_g.txt
wc -l query-cosientist.md >> /tmp/rank_g.txt 2>&1
echo DONE >> /tmp/rank_g.txt
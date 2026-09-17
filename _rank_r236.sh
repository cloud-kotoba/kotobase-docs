#!/bin/bash
# extract run236 portion from line 240
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
line=$(sed -n '240p' query-cosientist.md)
echo "$line" | grep -o 'run236A[^|]*' > /tmp/rank_run236.txt 2>&1
# also grab larger window around run236
echo "$line" | tr ' ' '\n' | grep -c 'run236' > /tmp/rank_run236_count.txt 2>&1
echo "$line" > /tmp/rank_line240b.txt
echo "DONE" >> /tmp/rank_run236.txt
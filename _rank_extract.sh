#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
awk 'NR==240' query-cosientist.md > /tmp/rank_line240.txt 2>&1
echo "DONE" >> /tmp/rank_line240.txt
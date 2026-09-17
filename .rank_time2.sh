#!/bin/bash
date '+%H:%M:%S JST' > .rank_time2.txt 2>&1
grep -c '^## Iteration log' /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md >> .rank_time2.txt 2>&1
grep -n '^## Iteration log' /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md >> .rank_time2.txt 2>&1
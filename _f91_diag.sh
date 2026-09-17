#!/bin/bash
echo "---tracked modifications---"
git -C /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs diff --name-only
echo "RC_DIFF=$?"
echo "---grep query-cosientist.md in status---"
grep -n "query-cosientist.md" /tmp/_f91_state.txt
echo "---recent log---"
git -C /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs log --oneline -8
echo "---load---"
uptime
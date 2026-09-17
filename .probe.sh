#!/bin/bash
echo "PROBE_START"
echo "cwd: $(pwd)"
date
git -C /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs log --oneline -5 2>&1
echo "PROBE_END"

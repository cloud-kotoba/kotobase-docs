#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > /tmp/kb_state1.txt 2>&1
echo "FETCH_RC=$?" >> /tmp/kb_state1.txt
git status >> /tmp/kb_state1.txt 2>&1
echo "===REMOTE===" >> /tmp/kb_state1.txt
git rev-parse net-kotobase/main >> /tmp/kb_state1.txt 2>&1
git rev-parse HEAD >> /tmp/kb_state1.txt 2>&1
echo "===LOG===" >> /tmp/kb_state1.txt
git log --oneline -8 >> /tmp/kb_state1.txt 2>&1
echo done
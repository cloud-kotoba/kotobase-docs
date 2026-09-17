#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > /tmp/bench141_push.txt 2>&1
echo "push rc=$?" > /tmp/bench141_pushrc.txt
git rev-parse net-kotobase/main >> /tmp/bench141_pushrc.txt 2>&1
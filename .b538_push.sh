#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git push net-kotobase HEAD:main > /tmp/b538_push.txt 2>&1
echo "PUSH_RC=$?" >> /tmp/b538_push.txt
git rev-parse HEAD >> /tmp/b538_push.txt
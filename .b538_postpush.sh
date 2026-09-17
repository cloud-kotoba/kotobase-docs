#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git fetch net-kotobase > /tmp/b538_postpush.txt 2>&1
echo "FETCH_RC=$?" >> /tmp/b538_postpush.txt
echo "---local HEAD---" >> /tmp/b538_postpush.txt
git rev-parse HEAD >> /tmp/b538_postpush.txt
echo "---remote main---" >> /tmp/b538_postpush.txt
git rev-parse net-kotobase/main >> /tmp/b538_postpush.txt
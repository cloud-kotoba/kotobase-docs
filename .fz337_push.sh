#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > /tmp/push_txt.txt 2>&1
echo "PUSHEXIT:$?" >> /tmp/push_txt.txt 2>&1
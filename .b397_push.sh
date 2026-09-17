#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git push net-kotobase HEAD:main > .b397_push.txt 2>&1
echo PUSH_RC=$? >> .b397_push.txt
git log --oneline -1 --format='%h %ci %s' >> .b397_push.txt
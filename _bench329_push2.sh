#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > .bench329_push2.txt 2>&1
echo "=== local HEAD ===" >> .bench329_push2.txt
git rev-parse HEAD >> .bench329_push2.txt 2>&1
echo "=== remote main ===" >> .bench329_push2.txt
git rev-parse net-kotobase/main >> .bench329_push2.txt 2>&1
LOCAL=$(git rev-parse HEAD)
REMOTE=$(git rev-parse net-kotobase/main)
echo "local=$LOCAL remote=$REMOTE" >> .bench329_push2.txt
if [ "$LOCAL" = "$REMOTE" ]; then
  echo "already-synced" >> .bench329_push2.txt
else
  git push net-kotobase HEAD:main > .bench329_push2.txt 2>&1
  echo "push_rc=$?" >> .bench329_push2.txt
fi
git rev-parse HEAD >> .bench329_push2.txt 2>&1
echo "push2_done" >> .bench329_push2.txt
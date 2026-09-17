#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git fetch net-kotobase >> .c152_commit.txt 2>&1
R=$(git rev-parse net-kotobase/main)
L=$(git rev-parse HEAD)
if [ "$R" != "$L" ]; then
  echo "DIVERGED remote=$R local=$L" >> .c152_commit.txt
  exit 2
fi
git add query-cosientist.md >> .c152_commit.txt 2>&1
git commit -m 'cosientist 153: K-Z3 1hr band-first run575A-C cold 11/60 (~18.3%), control 0/20 separated; iter/evidence update' >> .c152_commit.txt 2>&1
git push net-kotobase HEAD:main >> .c152_push.txt 2>&1
git fetch net-kotobase >> .c152_push.txt 2>&1
echo "post: local=$(git rev-parse HEAD) remote=$(git rev-parse net-kotobase/main)" >> .c152_push.txt

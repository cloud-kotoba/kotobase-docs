#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "== pre-push fetch =="
  git fetch net-kotobase main 2>&1
  echo "== HEAD =="
  git rev-parse HEAD
  echo "== remote =="
  git rev-parse net-kotobase/main
  echo "== add =="
  git add query-cosientist.md
  echo "== commit =="
  git commit -m "bench 第212回: K-Z3 17時台 n-add run487 cold 10/60 (control clean; 17時台通算 22/180 ~12.2% 3set) evidence+iter-log" 2>&1
  echo "== new HEAD =="
  git rev-parse HEAD
  echo "== push =="
  git push net-kotobase HEAD:main 2>&1
  echo "== post remote =="
  git rev-parse net-kotobase/main
} > /tmp/b487commit.txt 2>&1
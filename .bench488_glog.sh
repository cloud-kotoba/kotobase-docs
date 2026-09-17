#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "===== git log -6 ====="
  git log --oneline -6
  echo "===== hashes ====="
  git rev-parse HEAD
  echo "===== grep run486/run485/run487 in file ====="
  grep -c "run486" query-cosientist.md
  grep -c "run485" query-cosientist.md
  grep -c "run487" query-cosientist.md
} > /tmp/glog.txt 2>&1
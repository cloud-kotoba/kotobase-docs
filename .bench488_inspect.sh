#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "===== git log -12 oneline ====="
  git log --oneline -12
  echo "===== does falsify 217 commit exist? ====="
  git log --oneline --all | grep -i "217" | head -5
  echo "===== bench 211 full iter-log entry (line 407 exact) ====="
  sed -n '407p' query-cosientist.md
} > /tmp/inspect.txt 2>&1
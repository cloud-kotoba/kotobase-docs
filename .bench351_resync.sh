#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > .bench351_refetch.txt 2>&1
git rev-parse HEAD > .bench351_head.txt 2>&1
git rev-parse net-kotobase/main > .bench351_remote.txt 2>&1
git log --oneline -8 > .bench351_log.txt 2>&1
{
  echo "=== status (short) ==="
  git status --short | grep -v '^??' | head -20
  echo "=== in-flight run351 / f351 files ==="
  ls -la .b351* .f351* 2>/dev/null
  ls -la .f351* 2>/dev/null
  echo "=== date ==="
  date '+%Y-%m-%dT%H:%M:%S%z'
  uptime
} > .bench351_state.txt 2>&1
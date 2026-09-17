#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > .bench352_fetch.txt 2>&1
git rev-parse HEAD > .bench352_head.txt 2>&1
git rev-parse net-kotobase/main > .bench352_remote.txt 2>&1
git log --oneline -5 > .bench352_log.txt 2>&1
{
  echo "=== modified tracked files ==="
  git status --short | head -20
  echo "=== in-flight run351/352 files ==="
  ls -la .f351* .b351* 2>/dev/null
  ls -la .f352* 2>/dev/null
} > .bench352_state.txt 2>&1
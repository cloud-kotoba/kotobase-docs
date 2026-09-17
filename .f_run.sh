#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== now ==="
  date "+%Y-%m-%d %H:%M:%S %Z"
  echo "=== fetch net-kotobase ==="
  git fetch net-kotobase 2>&1 | tail -3
  echo "HEAD=$(git rev-parse HEAD)"
  echo "REMOTE=$(git rev-parse net-kotobase/main 2>&1)"
  echo "=== run321 collision check ==="
  grep -c "run321" query-cosientist.md
  echo "=== Iteration log newest 3 ==="
  grep -n "^## Iteration log" query-cosientist.md
  echo "=== host load now ==="
  uptime
  echo "=== live smoke ==="
  curl -s -o /dev/null -m 10 -w "landing %{http_code} %{time_total}s\n" https://kotobase.net/
  curl -s -o /dev/null -m 10 -w "signup %{http_code} %{time_total}s\n" https://kotobase.net/signup
} > .f_setup.txt 2>&1
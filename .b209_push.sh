#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== push net-kotobase ==="
  git push net-kotobase HEAD:main 2>&1
  echo "PUSH_NET_RC=$?"
  echo "=== push bench_fetch ==="
  git push bench_fetch HEAD:main 2>&1
  echo "PUSH_FETCH_RC=$?"
  sleep 2
  echo "=== local HEAD ==="
  git rev-parse HEAD
  echo "=== remote net-kotobase main ==="
  git rev-parse net-kotobase/main
  echo "=== remote bench_fetch main ==="
  git rev-parse bench_fetch/main 2>&1
} > /tmp/b209_push_out.txt 2>&1
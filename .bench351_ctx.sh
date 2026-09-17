#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== run351 context ==="
  grep -n "run351" query-cosientist.md
  echo "=== 13時台 context (line nos only via -n) ==="
  grep -n "13時台" query-cosientist.md
} > .bench351_ctx.txt 2>&1
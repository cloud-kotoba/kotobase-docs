#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "=== NEXT lines in iterlog top region (lines 360-366) ==="
  sed -n '360,366p' query-cosientist.md
} > .bench351_next.txt 2>&1
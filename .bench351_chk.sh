#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  echo "--- ls .b351* .f351* ---"
  ls -la .b351* .f351* 2>/dev/null
  echo "--- ls .b35* ---"
  ls -la .b35* 2>/dev/null
  echo "--- 13時台 count in HEAD ---"
  grep -c "13時台" query-cosientist.md
  echo "--- run351 count in HEAD ---"
  grep -c "run351" query-cosientist.md
  echo "--- run350 count in HEAD ---"
  grep -c "run350" query-cosientist.md
  echo "--- (end) ---"
} > .bench351_chk.txt 2>&1
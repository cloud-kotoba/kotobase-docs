#!/bin/bash
for d in /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane \
         /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine; do
  echo "== $d =="
  if [ -d "$d" ]; then ls "$d" | head -30; else echo "ABSENT"; fi
done > /tmp/cos_cp.txt 2>&1
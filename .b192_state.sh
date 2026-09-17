#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=/tmp/bench_state.txt
: > "$OUT"

{
echo "===DATE==="
date '+%Y-%m-%d %H:%M:%S %Z'
echo "===LOAD==="
uptime
echo "===FETCH==="
git fetch net-kotobase main 2>&1
echo "===STATUS==="
git status --short 2>&1
echo "===LOG_MAIN==="
git log --oneline -6 net-kotobase/main 2>&1
echo "===HEAD_LOCAL==="
git rev-parse HEAD 2>&1
echo "===HEAD_MAIN==="
git rev-parse net-kotobase/main 2>&1
} >> "$OUT" 2>&1
echo "STATE_WRITTEN"
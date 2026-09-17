#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/bench_tick1.out
echo "=== DATE ===" > "$OUT"
date '+%Y-%m-%d %H:%M:%S %Z' >> "$OUT"
echo "=== UPTIME ===" >> "$OUT"
uptime >> "$OUT"
echo "=== FETCH ===" >> "$OUT"
git fetch net-kotobase main 2>&1 >> "$OUT"
echo "=== LOG ===" >> "$OUT"
git log --oneline -5 >> "$OUT"
echo "=== STATUS ===" >> "$OUT"
git status --short | head -20 >> "$OUT"
echo "=== REVPARSE local ===" >> "$OUT"
git rev-parse HEAD >> "$OUT"
echo "=== REVPARSE remote ===" >> "$OUT"
git rev-parse net-kotobase/main 2>&1 >> "$OUT"
echo "=== DONE ===" >> "$OUT"
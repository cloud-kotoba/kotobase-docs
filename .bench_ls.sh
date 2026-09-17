#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
OUT=/tmp/bench_ls.out
echo "=== recent .sh/.py scratch scripts (ls -lt newest 40) ===" > "$OUT"
ls -lt .*.sh .*.py 2>/dev/null | head -40 >> "$OUT"
echo "=== any .b467* scratch ===" >> "$OUT"
ls -la .b467* 2>&1 >> "$OUT"
echo "=== DONE ===" >> "$OUT"
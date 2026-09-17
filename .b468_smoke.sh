#!/bin/sh
OUT=/tmp/bench_smoke.out
echo "=== smoke 13:39 ===" > "$OUT"
date '+%Y-%m-%d %H:%M:%S %Z' >> "$OUT"
echo "--- search.kotobase.net/search?q=test ---" >> "$OUT"
curl -s -o /dev/null -w 'search HTTP %{http_code} ttfb=%{time_starttransfer}s\n' --connect-timeout 10 --max-time 20 "https://search.kotobase.net/search?q=test" >> "$OUT"
echo "--- kotobase.net/signup ---" >> "$OUT"
curl -s -o /dev/null -w 'signup HTTP %{http_code} ttfb=%{time_starttransfer}s\n' --connect-timeout 10 --max-time 20 "https://kotobase.net/signup" >> "$OUT"
echo "--- kotobase.net/ ---" >> "$OUT"
curl -s -o /dev/null -w 'root HTTP %{http_code} ttfb=%{time_starttransfer}s\n' --connect-timeout 10 --max-time 20 "https://kotobase.net/" >> "$OUT"
echo "=== DONE ===" >> "$OUT"
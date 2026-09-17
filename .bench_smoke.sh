#!/bin/bash
{
curl -s -o /dev/null -w "search_code=%{http_code} ttfb=%{time_starttransfer}\n" --max-time 30 "https://search.kotobase.net/search?q=test"
curl -s -o /dev/null -w "root_code=%{http_code}\n" --max-time 30 "https://kotobase.net/"
curl -s -o /dev/null -w "signup_code=%{http_code}\n" --max-time 30 "https://kotobase.net/signup"
} > /tmp/bench_smoke.txt 2>&1
echo done
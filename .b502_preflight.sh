#!/bin/bash
# preflight for bench run502 (2026-09-08 20時台 4th set)
set -u
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b502_preflight.txt"
{
echo "=== time ==="
date '+%Y-%m-%d %H:%M:%S %Z'
echo "=== HEAD vs remote (git rev-parse) ==="
git rev-parse HEAD
git rev-parse net-kotobase/main
echo "=== worktree doc diff (should be empty) ==="
git status --short -- query-cosientist.md
echo "=== run502 already used in doc? (expect 0) ==="
grep -c "run502" query-cosientist.md || echo "run502 not found (count 0)"
echo "=== live smoke (/, /signup, search) ==="
curl -s -o /dev/null -w "/ %{http_code}\n" --max-time 15 "https://kotobase.net/"
curl -s -o /dev/null -w "/signup %{http_code}\n" --max-time 15 "https://kotobase.net/signup"
curl -s -o /dev/null -w "/search %{http_code}\n" --max-time 15 "https://search.kotobase.net/search?q=test"
echo "=== uptime ==="
uptime
} > "$OUT" 2>&1
echo "written"
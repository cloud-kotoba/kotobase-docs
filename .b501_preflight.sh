#!/bin/bash
# preflight: git state, DNS, run501 used-check, endpoint reachability
set -u
OUT="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b501_preflight.txt"
{
echo "=== HEAD vs remote (git rev-parse) ==="
git rev-parse HEAD
git rev-parse net-kotobase/main
git rev-parse FETCH_HEAD
echo "=== worktree doc diff (should be empty) ==="
git status --short -- query-cosientist.md
echo "=== run501 already used in doc? (expect 0) ==="
grep -c "run501" query-cosientist.md || echo "run501 not found (count 0)"
echo "=== DNS search.kotobase.net ==="
getent hosts search.kotobase.net 2>/dev/null || nslookup search.kotobase.net 2>&1 | head -5
echo "=== live smoke (/, /signup, search) ==="
curl -s -o /dev/null -w "/ %{http_code}\n" --max-time 15 "https://kotobase.net/"
curl -s -o /dev/null -w "/signup %{http_code}\n" --max-time 15 "https://kotobase.net/signup"
curl -s -o /dev/null -w "/search %{http_code}\n" --max-time 15 "https://kotobase.net/search?q=test"
echo "=== uptime ==="
uptime
} > "$OUT" 2>&1
echo "written"
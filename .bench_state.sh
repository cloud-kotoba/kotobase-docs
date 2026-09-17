#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD iter-log entry (last 3 bullets) ==="
grep -nE "^- 2026-09-0[78]:" query-cosientist.md | tail -6
echo ""
echo "=== run410 / run411 mentions ==="
grep -n "run411\|run410" query-cosientist.md | tail -12
echo ""
echo "=== last 5 lines of Iteration log section ==="
grep -n "^## Iteration log" query-cosientist.md
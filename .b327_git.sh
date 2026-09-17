#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== FETCH ==="
git fetch bench_fetch 2>&1 | tail -5
echo "=== HEAD_REV ==="
git rev-parse HEAD
echo "=== REMOTE_REV ==="
git rev-parse bench_fetch 2>/dev/null || git rev-parse bench_fetch/main
echo "=== STATUS ==="
git status --short | head -30
echo "=== LOG_HEAD (falsify/bench latest) ==="
git log --oneline -15
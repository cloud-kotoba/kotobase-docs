#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== date ==="
date
echo "=== git HEAD ==="
git rev-parse HEAD
echo "=== fetch ==="
git fetch net-kotobase main 2>&1 | head -5
echo "fetch rc=$?"
echo "=== remote main ==="
git rev-parse net-kotobase/main 2>&1
echo "=== run360 / b360 collision check ==="
ls -la .b360* 2>&1 | head -20
ls -la .b359* 2>&1 | head -20
echo "=== uncommitted in query-cosientist.md? ==="
git status --short query-cosientist.md
echo "=== recent bench/falsify scripts to reuse ==="
ls -la .b356*.sh .b357*.sh .b358*.sh .b359*.sh 2>&1 | head -30
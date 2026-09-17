#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase main > .bench329_verify2.txt 2>&1
echo "remote=$(git rev-parse net-kotobase/main)" >> .bench329_verify2.txt
echo "head=$(git rev-parse HEAD)" >> .bench329_verify2.txt
echo "=== status query-cosientist ===" >> .bench329_verify2.txt
git status --short query-cosientist.md >> .bench329_verify2.txt 2>&1
echo "=== last 3 log ===" >> .bench329_verify2.txt
git log --oneline -3 >> .bench329_verify2.txt 2>&1
echo "verify2_done" >> .bench329_verify2.txt
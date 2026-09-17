#!/bin/bash
date '+%Y-%m-%d %H:%M:%S %Z' > /tmp/bench_start.txt
echo "--- git log ---" >> /tmp/bench_start.txt
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs && git log --oneline -8 >> /tmp/bench_start.txt 2>&1
echo "--- git status ---" >> /tmp/bench_start.txt
git status >> /tmp/bench_start.txt 2>&1
echo "--- NEXT lines ---" >> /tmp/bench_start.txt
grep -n "NEXT:" query-cosientist.md >> /tmp/bench_start.txt 2>&1
echo "--- done ---" >> /tmp/bench_start.txt
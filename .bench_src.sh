#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
grep -n "K-Z3" query-cosientist.md > /tmp/bench_kz3.txt
echo "=== ITER LOG HEAD (first 25 lines of Iteration log) ===" >> /tmp/bench_kz3.txt
awk '/## Iteration log/{f=1} f&&c<30{print NR": "$0; c++}' query-cosientist.md >> /tmp/bench_kz3.txt
echo "=== DONE ===" >> /tmp/bench_kz3.txt
#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== run271 occurrences in K-Z3 row ==="
grep -oF 'run271' query-cosistentist.md >/dev/null 2>&1
awk 'NR==260' query-cosistentist.md 2>/dev/null | grep -oF 'run271' | wc -l
awk 'NR==260' query-cosistentist.md 2>/dev/null | grep -oF 'run271A' | wc -l
echo "=== does line 260 mention run271 fold? grep whole file run271A ==="
grep -oF 'run271A' query-cosistentist.md | wc -l
echo "=== positions of run271 (byte offset) in line 260 tail ==="
awk 'NR==260' query-cosistentist.md 2>/dev/null | grep -boF 'run271' | tail -3
echo "=== printable ascii count in last 1500 bytes ==="
awk 'NR==260' query-cosistentist.md 2>/dev/null | tail -c 1500 | tr -cd '[:print:]\n' | wc -c
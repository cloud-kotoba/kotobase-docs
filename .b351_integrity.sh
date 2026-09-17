#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
F=query-cosientist.md
{
echo "=== wc ==="
wc -l "$F"
echo "=== rank157 head present? ==="
grep -c '^\- 2026-09-07: rank 第157回。14:59 JST tick' "$F"
echo "=== rank157 tail present? (run364) ==="
grep -c 'run ID は run364 使用' "$F"
echo "=== rank157 line tail (last 80 chars) ==="
python3 .b351_tail.py
} > .b351_integrity.txt 2>&1
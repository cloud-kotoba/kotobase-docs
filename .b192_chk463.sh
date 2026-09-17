#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
OUT=/tmp/bench_chk463.txt
: > "$OUT"
{
echo "===run463_in_committed_HEAD==="
git show HEAD:query-cosientist.md 2>/dev/null | grep -c "run463"
echo "===f208_in_committed_HEAD==="
git show HEAD:query-cosientist.md 2>/dev/null | grep -c "第208回"
echo "===iterlog_uncommitted (working tree)==="
grep -n "第208回\|run463" query-cosientist.md 2>/dev/null | head -20
echo "===END==="
} >> "$OUT" 2>&1
echo "CHK_DONE"
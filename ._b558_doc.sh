#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
git show HEAD:query-cosientist.md > /tmp/qc_head.md 2>/dev/null || cp query-cosientist.md /tmp/qc_head.md
{
echo "=== HEAD copy lines ==="
wc -l < /tmp/qc_head.md
echo "=== search?q=test occurrences in git HEAD ==="
git show HEAD:query-cosientist.md | grep -c 'search?q=test'
echo "=== recent bench run lines ==="
git show HEAD:query-cosientist.md | grep -n 'run54[6-9]\|run55[0-9]' | tail -30
echo "=== K-Z3 row ==="
git show HEAD:query-cosientist.md | grep -n '| K-Z3' | head -3
} > ._b558_doc_out.txt 2>&1

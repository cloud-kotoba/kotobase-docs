#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD pre ==="
git rev-parse HEAD
echo "=== NUMSTAT ==="
git diff HEAD --numstat -- query-cosientist.md
echo "=== DIFFSTAT ==="
git diff HEAD --stat -- query-cosientist.md
echo "=== HDR+RANK order check ==="
grep -c "^## Iteration log$" query-cosientist.md
awk 'BEGIN{n=0} /^## Iteration log$/{n++} /rank 第195回/{r=1} /falsify 第196回/{f=1} END{print "hdr="n, "rank195="r, "falsify196="f}' query-cosientist.md
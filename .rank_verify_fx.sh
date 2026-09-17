#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch bench_fetch 2>&1
echo "=== bench_fetch/main HEAD ==="
git rev-parse bench_fetch/main
echo "=== local HEAD ==="
git rev-parse HEAD
echo "=== adv/behind ==="
git rev-list --left-right --count HEAD...bench_fetch/main 2>&1
echo "=== remote blob rank195 present ==="
git show bench_fetch/main:query-cosientist.md | grep -c "rank 第195回。08:40"
echo "=== remote blob header count ==="
git show bench_fetch/main:query-cosientist.md | grep -c "^## Iteration log$"
echo "=== remote blob order ==="
git show bench_fetch/main:query-cosientist.md | awk 'BEGIN{n=0} /^## Iteration log$/{n++} /rank 第195回/{r=1} /falsify 第196回/{f=1} END{print "hdr="n, "rank195="r, "falsify196="f}'
#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "bench 110: K-Z3 24hr(0hr) n-add run272A-C cold 2/60 ~3.3% (run272A scatter 1.16s/1.43s, B/C 0/20 vanish, control 0.042s max 0.059s fully quiet sep established, cold localized to search; 24hr total run268+269+270+271+272 = 15/300 ~5.0% 5-set contiguous cold>0, low position within heavy re-rise amplitude; traffic-independence counter-evidence continues; status/rank to rank)" > /tmp/bench_commit272.txt 2>&1
echo "commit exit=$?" >> /tmp/bench_commit272.txt
git rev-parse --short HEAD >> /tmp/bench_commit272.txt
echo "=== push ===" >> /tmp/bench_commit272.txt
git push net-kotobase HEAD:main > /tmp/bench_push272.txt 2>&1
echo "push exit=$?" >> /tmp/bench_push272.txt
git rev-parse --short HEAD >> /tmp/bench_push272.txt
git fetch net-kotobase >/dev/null 2>&1
echo "origin now:" >> /tmp/bench_push272.txt
git rev-parse --short net-kotobase/main >> /tmp/bench_push272.txt
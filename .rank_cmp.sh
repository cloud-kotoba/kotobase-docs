#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
echo "===LOCAL_HEAD==="
git rev-parse HEAD
echo "===BENCH_FETCH_MAIN==="
git rev-parse bench_fetch/main 2>&1
echo "===NET_MAIN==="
git rev-parse net-kotobase/main 2>&1
echo "===LOG_ON_MAIN_10==="
git log --oneline bench_fetch/main -10
echo "===DIFF_LOCAL_VS_FETCHMAIN==="
git rev-list --count HEAD..bench_fetch/main 2>&1
echo "===MANIFEST_TAIL==="
ls -la manifest* 2>&1 | head
} > .rank_cmp.txt 2>&1
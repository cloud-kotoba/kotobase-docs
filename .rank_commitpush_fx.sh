#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
echo "=== staged ==="
git diff --cached --numstat -- query-cosientist.md
git commit -m "rank 195th: fold falsify195-run440 + bench195-run441 + falsify196-run442 -> 8hr 6/300 ~2.0% low band; status/rank/evolve unchanged; NEXT K-Z3 8hr n-add run443" > /tmp/rank_commit_out.log 2>&1
echo "=== commit rc + head ==="
git rev-parse HEAD
echo "=== push bench_fetch ==="
git push bench_fetch HEAD:main 2>&1
echo "=== push rc logged ==="
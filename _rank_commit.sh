#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===LIVE sibling procs (rank/falsify/bench/cosient)==="
ps aux 2>/dev/null | grep -iE 'net-kotobase-(rank|falsify|bench|cosient)' | grep -v grep | grep -v 'bash-language-server' | head
echo "===COMMITTED log tail at HEAD 80c405c==="
git show HEAD:query-cosientist.md 2>&1 | grep -n '^## Iteration log' 
echo "===committed iteration log first entry==="
git show HEAD:query-cosientist.md 2>&1 | sed -n '/## Iteration log/,/^## .*第10/p' | head -8
echo "===K-Z3 row 20時台 in committed HEAD==="
git show HEAD:query-cosientist.md 2>&1 | grep -o '20時台通算 [0-9/]*[~%0-9.]*' | tail -5
echo "===HEAD K-Z3 tail==="
git show HEAD:query-cosientist.md 2>&1 | grep -c 'run243'
echo "===NEXT in committed HEAD==="
git show HEAD:query-cosientist.md 2>&1 | grep -o 'NEXT[:：]*[^
]*' | tail -3
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== is 286b9b5 ancestor of HEAD b616d8e ? ==="
git merge-base --is-ancestor 286b9b5 HEAD && echo "YES_286_ancestor" || echo "NO"
echo "=== is cbbeac1 ancestor of b616d8e ? ==="
git merge-base --is-ancestor cbbeac1 HEAD && echo "YES_cbbeac1_ancestor" || echo "NO"
echo "=== is 75dadd5 ancestor of HEAD ? ==="
git merge-base --is-ancestor 75dadd5 HEAD && echo "YES_75_ancestor" || echo "NO_75_not_ancestor"
echo "=== bench_fetch/main vs HEAD merge-base ==="
git rev-parse 286b9b5 2>&1
echo "=== net-kotobase/main 75dadd5 log -3 ==="
git log --oneline -3 75dadd5 2>&1
echo "=== fetch refspec net-kotobase ==="
git config --get-all remote.net-kotobase.fetch 2>&1
echo "=== fetch refspec bench_fetch ==="
git config --get-all remote.bench_fetch.fetch 2>&1
echo "=== net-kotobase HEAD ref ==="
git symbolic-ref refs/remotes/net-kotobase/HEAD 2>&1
echo "=== END ==="
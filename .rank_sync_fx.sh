#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== CURR HEAD ==="
git rev-parse HEAD
echo "=== LOG -4 ==="
git log --oneline -4
echo "=== FETCH bench_fetch ==="
git fetch bench_fetch 2>&1
echo "=== LOG bench_fetch/main -4 ==="
git log --oneline bench_fetch/main -4
echo "=== DIFF HEAD vs worktree ==="
git diff HEAD --stat -- query-cosientist.md
echo "=== HEAD blob contains falsify196? ==="
git show HEAD:query-cosientist.md | grep -c "falsify 第196回\|falsify 第195回\|bench 第195回"
echo "=== worktree newest iter lines 400-410 ==="
sed -n '400,412p' query-cosientist.md
echo "=== header line ==="
grep -n "^## Iteration log" query-cosientist.md
echo "=== adv/behind ==="
git rev-list --left-right --count HEAD...bench_fetch/main 2>&1
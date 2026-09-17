#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== HEAD ==="
git rev-parse HEAD 2>&1
echo "=== HEAD subject ==="
git log -1 --format='%s' 2>&1
echo "=== net-kotobase/main ==="
git rev-parse refs/remotes/net-kotobase/main 2>&1
echo "=== divergence check (md tracked) ==="
git status --short query-cosientist.md 2>&1
echo "=== md tracked file clean? (no output above = clean) ==="
echo "=== last 6 iteration entries (grep rank/falsify/bench/cosientist 第) ==="
grep -oE '(^|-) (rank|falsify|bench|cosientist) 第[0-9]+回' query-cosientist.md | head -8
echo "=== confirm rank116 tail present ==="
grep -oE 'NEXT: K-Z3 23時台 n 積み増し継続 — 23時台は 8 セット通算 25/480' query-cosientist.md | head -1
echo "=== END ==="
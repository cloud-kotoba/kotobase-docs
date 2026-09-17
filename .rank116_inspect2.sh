#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== parent of b616d8e ==="
git log -3 --format='%h %p %s' b616d8e 2>&1
echo "=== diff b616d8e vs its parent (what did MY commit add) ==="
git show --stat b616d8e 2>&1 | head -20
echo "=== diff b616d8e vs 75dadd5 (what differs from remote) ==="
git diff --stat b616d8e 75dadd5 2>&1
echo "=== does b616d8e re-add falsify121 evidence? search run266 in b616d8e md ==="
git show b616d8e:query-cosientist.md | grep -c 'run266' 2>&1
echo "=== does 75dadd5 md have run266 and rank116? ==="
git show 75dadd5:query-cosientist.md | grep -c 'run266' 2>&1
git show 75dadd5:query-cosientist.md | grep -c 'rank 第116回' 2>&1
echo "=== does b616d8e have rank116 once? ==="
git show b616d8e:query-cosientist.md | grep -c 'rank 第116回' 2>&1
echo "=== merge-base b616d8e 75dadd5 ==="
git merge-base b616d8e 75dadd5 2>&1
echo "=== END ==="
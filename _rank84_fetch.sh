#!/bin/bash
# rank 84: fetch + divergence check
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
echo "=== rank84 sync check ==="
date
git fetch net-kotobase 2>&1
echo "FETCH_RC=$?"
echo "HEAD=$(git rev-parse HEAD)"
echo "MAIN=$(git rev-parse net-kotobase/main)"
if git merge-base --is-ancestor net-kotobase/main HEAD; then
  echo "ANC_RC=0 (up to date)"
else
  echo "ANC_RC=1 (behind)"
fi
echo "--- new commits (HEAD..main) ---"
git log --oneline HEAD..net-kotobase/main
echo "=== done ==="

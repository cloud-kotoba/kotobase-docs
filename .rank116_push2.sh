#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== push to net-kotobase remote main ==="
git push net-kotobase b616d8e183f130e5b41f849f5d4baf0571bbde97:main 2>&1
echo "push_rc=$?"
echo "=== re-fetch to confirm remote main updated ==="
git fetch net-kotobase 2>&1
echo "fetch_rc=$?"
echo "=== net-kotobase/main now ==="
git rev-parse refs/remotes/net-kotobase/main 2>&1
echo "=== our HEAD ==="
git rev-parse HEAD 2>&1
echo "=== END ==="
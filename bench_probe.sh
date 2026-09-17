#!/bin/sh
echo "=== probe ==="
uname -a
date '+%F %T %z'
echo "=== git ==="
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
git rev-parse --short HEAD
git pull --ff-only 2>&1
echo "PULL_EXIT=$?"

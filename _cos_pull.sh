#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
echo "--- pull --ff-only ---"
git pull --ff-only net-kotobase main 2>&1
echo "PULL_RC=$?"
echo "--- HEAD now ---"
git log --oneline -3
echo "--- divergence vs net-kotobase/main ---"
git rev-list --left-right --count HEAD...net-kotobase/main 2>&1
} > /tmp/cos_pull.txt 2>&1
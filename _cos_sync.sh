#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 1
{
echo "PWD: $(pwd)"
echo "--- fetch ---"
git fetch origin 2>&1
echo "FETCH_RC=$?"
echo "--- HEAD ---"
git rev-parse HEAD
git log --oneline -5
echo "--- branch ---"
git rev-parse --abbrev-ref HEAD
echo "--- diff vs origin/main ---"
git rev-list --count HEAD..origin/main 2>&1
} > /tmp/cos_sync_out.txt 2>&1
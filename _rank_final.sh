#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===NOW==="
date "+%H:%M:%S"
echo "===HEAD==="
git rev-parse --short HEAD
echo "===porcelain (non-untracked)==="
git status --porcelain | grep -v '^??' | head -5
echo "===file mtime==="
stat -f "%Sm" -t "%H:%M:%S" query-cosientist.md
echo "---wait 4s---"
sleep 4
echo "===NOW2==="
date "+%H:%M:%S"
stat -f "%Sm" -t "%H:%M:%S" query-cosientist.md
echo "===reflog -2==="
git reflog -2
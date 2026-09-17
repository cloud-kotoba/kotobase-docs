#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "===NOW==="
date "+%H:%M:%S"
echo "===ANY hermes/cron/node procs (full)==="
ps aux 2>/dev/null | grep -iE 'hermes|cron|net-kotobase' | grep -v grep | grep -v 'bash-language-server' | grep -iv 'CoreAudio|distnoted|coreaudio' | head -25
echo "===query-cosientist.md mtime==="
stat -f "%Sm" -t "%H:%M:%S" query-cosientist.md
echo "===staged diff mtime of index==="
stat -f "%Sm" -t "%H:%M:%S" .git/index
echo "===last commits by time==="
git log --format='%h %ci %s' -6 2>&1
echo "===git status porcelain 1st 2 lines==="
git status --porcelain 2>&1 | head -3
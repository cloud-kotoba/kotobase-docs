#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
printf 'PWD: '; pwd
printf 'HEAD:\n'; git log --oneline -5 2>&1
printf 'STATUS:\n'; git status --short 2>&1
printf 'MTIME:\n'; ls -la query-cosientist.md
#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git diff --stat query-cosientist.md > .bench351_diffstat.txt 2>&1
git status --short | grep -v '^??' > .bench351_mod.txt 2>&1
git diff --numstat query-cosientist.md >> .bench351_mod.txt 2>&1
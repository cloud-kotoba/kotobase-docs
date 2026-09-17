#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git diff query-cosientist.md > .b351_diff.txt 2>&1
echo done > .b351_diff_done.txt
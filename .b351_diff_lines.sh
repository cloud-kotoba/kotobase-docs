#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
F=query-cosientist.md
git diff "$F" | grep '^[+-]' | grep -v '^[+-][+-]' | python3 -c '
import sys
for i,l in enumerate(sys.stdin,1):
    s=l.rstrip("\n")
    print(i, s[:90].replace("\n"," "))
' > .b351_diff_lines.txt 2>&1
echo "=== count ===" >> .b351_diff_lines.txt
git diff --numstat "$F" >> .b351_diff_lines.txt 2>&1
#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
python3 .b351_fixdup.py > .b351_fixdup.txt 2>&1
echo "rc=$?" >> .b351_fixdup.txt
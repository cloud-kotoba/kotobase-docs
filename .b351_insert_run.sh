#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
python3 .b351_insert.py > .b351_insert.txt 2>&1
echo "rc=$?" >> .b351_insert.txt
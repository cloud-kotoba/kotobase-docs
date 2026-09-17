#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
grep -n "Iteration log" query-cosientist.md > .rank_iloc.txt 2>&1
grep -n "第1[0-9][0-9]回\|第9[0-9]回\|第8[0-9]回" query-cosientist.md > .rank_ihdr.txt 2>&1
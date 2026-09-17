#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=====ITER-HEAD====="
grep -n "^## Iteration log" query-cosientist.md
echo "=====ITER-ENTRIES====="
grep -n "^\* 2026-09-0" query-cosientist.md | tail -8
echo "=====NEW-HYPOTHESIS-ANCHOR====="
grep -n "K-Z\|NEXT:" query-cosientist.md | tail -20
echo "=====DONE====="
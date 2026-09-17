#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md
git commit -m "bench 第178回: K-Z3 21hr band-first run397 (cold 0/1/2 = 3/60 ~5.0% A0/B1/C2, control borderline 0.50s -> not-separated-leaning; 21hr 帯初計測) + iter-log" > .b397_commit.txt 2>&1
git log --oneline -1 --format='%h %ci %s' >> .b397_commit.txt 2>&1
echo DONE > .b397_commit_done.txt
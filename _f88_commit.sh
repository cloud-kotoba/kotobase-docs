#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase > /tmp/f88_f2.txt 2>&1
echo "HEAD: $(git rev-parse HEAD)"
echo "MAIN: $(git rev-parse net-kotobase/main)"
git add query-cosientist.md
git commit -m "falsify 第88回: K-Z3 14時台 n 積み増し run213A-C (cold 4/60, control 分離成立) + iteration log" > /tmp/f88_c.txt 2>&1
echo "commit rc=$?"
git rev-parse HEAD > /tmp/f88_h.txt 2>&1
git push net-kotobase HEAD:main > /tmp/f88_p.txt 2>&1
echo "push rc=$?"
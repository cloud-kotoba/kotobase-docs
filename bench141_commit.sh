#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git add query-cosientist.md bench141_kz3_append2.py kz3_run333.sh kz3_run333_calc.py kz3_run333_out.txt kz3_run333_calc_out.txt kz3_run333_time.txt bench141_append_out.txt > /tmp/bench141_add.txt 2>&1
git commit -m "bench 141: K-Z3 10時台(9/7) run333A-C n-add cold 5/60 (A 4/20 cluster 1.18-2.06s / B 1/20, C 0/20), control 0/20 sep; 10時台通算 9/120 ~7.5% 中位帯, run331A heavy 9/20 弱後続; iteration log" > /tmp/bench141_cmt.txt 2>&1
echo "commit rc=$?" > /tmp/bench141_rc.txt
git rev-parse HEAD >> /tmp/bench141_rc.txt 2>&1
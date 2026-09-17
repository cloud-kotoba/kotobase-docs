#!/bin/bash
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs || exit 9
git show HEAD:query-cosientist.md > .b189_qc_base.md 2>.b189_gs.log
echo "gs_exit=$?" >> .b189_extract_out.txt
python3 .b189_extract2.py > .b189_extract_out.txt 2>&1
echo "extract_exit=$?" >> .b189_extract_out.txt
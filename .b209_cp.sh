#!/bin/sh
# commit + push bench 第209回 run481 evidence
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
{
  git add query-cosientist.md
  git commit -m "bench 第209回: K-Z3 16時台 n-add run481 cold 3/60 ~5.0% (run480 falsify先行->run481 読替; control 静穏分離成立; 16時台 3セット通算 14/180 ~7.8%) evidence+iter-log"
  echo "COMMIT_RC=$?"
  git rev-parse HEAD
} > /tmp/b209_cp_out.txt 2>&1
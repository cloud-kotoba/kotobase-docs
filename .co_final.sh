#!/bin/sh
cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
# Ensure only the state doc is staged (never the untracked .b3xx/_b1xx scratch/tmp files).
git add query-coscientist.md
# Commit (idempotent: nothing new staged -> "nothing to commit", rc != success but no harm).
git commit -q -m "cosientist 第124回: K-Z3 13時台 run356 n積み増し (cold 5/60 ~8.3%, run356A 5/20 散発クラスタ再上振れ, B/C+control 0/60 即消滅分離成立; 帯内1窓即消滅継続, 13時台通算 19/360 ~5.3% 6-set; qualify 0 実装なし) + iterlog" 2>&1
echo "COMMIT_RC=$?" > /tmp/co_final_result.txt
git log --oneline -1 >> /tmp/co_final_result.txt 2>&1
git status --short >> /tmp/co_final_result.txt 2>&1
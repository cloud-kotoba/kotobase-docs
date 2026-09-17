cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
echo "=== pre-commit fetch/rev ===" > .b396_commit.txt
git fetch net-kotobase main >> .b396_commit.txt 2>&1
git rev-parse HEAD >> .b396_commit.txt
git rev-parse net-kotobase/main >> .b396_commit.txt
echo "=== add+commit ===" >> .b396_commit.txt
git add query-cosientist.md >> .b396_commit.txt 2>&1
git commit -m "bench 第177回: K-Z3 20hr n-add run396 (cold 3/60 ~5.0% A 冒頭集中 3/20 deep 2.07s, B/C+control 0 完全静穏分離成立, collision-free; 20hr 通算 20/300 ~6.7% 中位帯候補) + iter-log" >> .b396_commit.txt 2>&1
echo "commit rc=$?" >> .b396_commit.txt
git rev-parse HEAD >> .b396_commit.txt
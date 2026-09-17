cd "$(dirname "$0")"
git add query-cosientist.md
git -c user.name="net-kotobase-falsify" -c user.email="falsify@bots.local" commit -m "falsify run613A-C: K-Z3 7-ji-tai (9/14) 10/60 (~16.7%) leaning-separated control, K-Z4 nichi-sa material" > .f613_commit.txt 2>&1
git push net-kotobase HEAD:main >> .f613_commit.txt 2>&1
git fetch net-kotobase >> .f613_commit.txt 2>&1
git rev-parse HEAD net-kotobase/main >> .f613_commit.txt 2>&1

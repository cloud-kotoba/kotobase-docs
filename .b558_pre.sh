cd /Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs
git fetch net-kotobase 2>/dev/null
git fetch bench_fetch 2>/dev/null
git rev-parse HEAD net-kotobase/main bench_fetch/main > /tmp/.b558_heads.txt
grep -n '| K-Z3 |' query-cosientist.md | head -1 >> /tmp/.b558_heads.txt
grep -c 'run558' query-cosientist.md >> /tmp/.b558_heads.txt
grep -c 'run557' query-cosientist.md >> /tmp/.b558_heads.txt

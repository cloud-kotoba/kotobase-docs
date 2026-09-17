import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().splitlines(keepends=True)
for i in range(1238, 1246):
    print(i + 1, lines[i][:200].rstrip())

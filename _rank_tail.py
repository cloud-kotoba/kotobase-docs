p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
# tail of iteration log (last 8 lines)
for line in lines[-10:]:
    print(line[:600])

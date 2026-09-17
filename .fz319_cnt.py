import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
for i,l in enumerate(lines):
    if "run319A cold 3/20" in l:
        print("at", i, "len", len(l))
        # show a window around first occurrence
        idx = l.find("run319A cold 3/20")
        print("  ctx:", repr(l[max(0,idx-40):idx+80]))
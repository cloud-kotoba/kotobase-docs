#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(p, encoding="utf-8") as f:
    lines = f.read().split("\n")
for i, l in enumerate(lines, 1):
    if l.startswith("| K-Z3 |"):
        print("K-Z3 row at L%d, len=%d" % (i, len(l)))
        print("HEAD80:", repr(l[:80]))
        print("TAIL100:", repr(l[-100:]))
        # does it end with a pipe?
        print("ends_with_pipe:", l.rstrip().endswith("|"))
        # count pipes
        print("pipe_count:", l.count("|"))
        break
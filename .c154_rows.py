import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    for i, ln in enumerate(f, 1):
        if ln.startswith("| K-Z3 | worker |"):
            tail = ln.rstrip()[-30:]
            print(i, repr(tail))

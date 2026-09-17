import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
lines = src.split("\n")
for i, ln in enumerate(lines, 1):
    if ln.startswith("| K-Z2 | worker |"):
        print("K-Z2 row at line", i, "len", len(ln))
        # print the tail (last 500 chars) to see current end of evidence
        print("...TAIL:", ln[-600:])
    if ln.startswith("| K-Z3 | worker |") or ln.startswith("| K-Q1 | query |"):
        print("row at line", i, "len", len(ln))

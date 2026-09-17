p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
# K-Z3 row at 278 (0-based). Evidence cell continues as subsequent lines until a line that starts a NEW hypothesis row or ##.
KZ3 = 278
# scan from KZ3+1 to find where this table cell ends.
# The cell continues while lines do NOT start with '|' followed by a hypothesis id like '| K-'.
# Actually entries are bare lines (continuation). Find the last evidence then the cell-closing line.
print("== lines 350-360 (0-based) start ==")
for i in range(350, 361):
    if i < len(lines):
        print(i, repr(lines[i][:70]))
print("== run318 references ==")
for i,l in enumerate(lines):
    if "run318" in l:
        print(i, l[:80])
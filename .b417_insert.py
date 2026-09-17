import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    data = f.read()
with io.open("/tmp/f417_add.txt", "r", encoding="utf-8") as f:
    add = f.read()
add = add.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
anchor = "sibling run415 は同一帯 independent 計測のため rank 判定の取込対象)。"
c = data.count(anchor)
if c != 1:
    print("ANCHOR_COUNT", c)
else:
    out = data.replace(anchor, anchor + add, 1)
    tally = out.count("run417")
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(out)
    print("OK", "run417_count", tally)
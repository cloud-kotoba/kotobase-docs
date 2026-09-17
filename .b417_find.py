import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    data = f.read()
anchor = "sibling run415 は同一帯 independent 計測のため rank 判定の取込対象)。"
pos = -1
count = 0
while True:
    pos = data.find(anchor, pos + 1)
    if pos < 0:
        break
    count += 1
    s = pos + len(anchor)
    seg = data[s:s+80]
    print("POS", pos, "AFTER", repr(seg))
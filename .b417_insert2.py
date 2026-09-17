import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    data = f.read()
with io.open("/tmp/f417_add.txt", "r", encoding="utf-8") as f:
    add = f.read()
add = add.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
anchor = "sibling run415 は同一帯 independent 計測のため rank 判定の取込対象)。"
pos = data.find(anchor)
if pos < 0:
    print("NO_ANCHOR")
else:

    a = len(anchor)
    p2 = pos + a
    after = data[p2:p2+12]
    ok = after.startswith("\n   bench")
    if not ok:
        print("WRONG_POSITION", repr(after))
    else:
        out = data[:p2] + add + data[p2:]
        with io.open(p, "w", encoding="utf-8") as f:
            f.write(out)
        print("OK", "run417_count", out.count("run417"))
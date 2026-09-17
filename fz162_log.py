import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

anchor = None
for i, ln in enumerate(lines):
    if ln.startswith("- 2026-09-05: falsify 第59回。"):
        anchor = i
        break
assert anchor is not None, "anchor not found"

entry = ("- 2026-09-05: falsify 第60回。rank 第52回 NEXT (委ねる) を受け、K-Z3 19時台帯 n 積み増し run162A–C を同測定法で実施 "
         "(19:02 JST, production HTTP 実測のため gate 外, secret 不含): search cold 0/60 完全静穏 (p50 49–76ms 帯), "
         "19時台通算 (2026-09-04 run88 分と合算) search cold 0/120 の低位帯。ただし landing control cold 2/20 (0.776s/0.619s 散発) で "
         "cold 群が landing 側にのみ出現する search 局在の逆転パターン — 分離成立だが方向逆転の稀なサンプル。"
         "18時台 (低位) → 19時台 (低位) → 21時台 (高位) の中間帯として 19時台は低位を維持。"
         "status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先)。\n")

lines.insert(anchor, entry)

with io.open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

with io.open("fz162_log.txt", "w", encoding="utf-8") as f:
    f.write("inserted before line %d\n" % (anchor + 1))

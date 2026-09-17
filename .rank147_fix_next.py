#!/usr/bin/env python3
path = "query-cosientist.md"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
old1 = "NEXT: K-Z3 current-band(現時刻帯 11時台) n-add 継続 (次 run ID は run339; 11時台が帯初なら帯初計測、済みなら n 積み増し、falsify 第88回/154回 precedent に従う)。secret は一切記録せず。"
new1 = "NEXT: K-Z3 current-band(現時刻帯 11時台) n-add 継続 (次 run ID は run340 — 本 tick 同時実行の falsify 第158回 (11:05, run339, 11時台帯初計測 cold 4/60) が run339 を先行測定済みのため、11時台は帯初計測済み → 次の観測枠は n 積み増し run340, falsify 第88回/154回 precedent に従う)。secret は一切記録せず。"
assert content.count(old1) == 1, "old NEXT not unique/found"
content = content.replace(old1, new1)
with open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("next updated")
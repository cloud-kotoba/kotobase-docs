s = open("query-cosientist.md", encoding="utf-8").read()

old = "積み増し継続 — 17時台帯初計測 1 セット 3/60 済みのため n 積み増し継続)。- 2026-09-06: falsify 第97回"
new = "積み増し継続 — 17時台帯初計測 1 セット 3/60 済みのため n 積み増し継続。※本 bench run226 と falsify 第97回 run226 は ID 衝突の独立 2 計測 — run105/run123/run193/run216/run224 前例に従い両方採用 (bench 17:01:17 3/60 / falsify 17:02:07 0/60)。)\n- 2026-09-06: falsify 第97回"

assert old in s, "concat anchor not found"
s = s.replace(old, new, 1)
open("query-cosientist.md", "w", encoding="utf-8").write(s)
print("fixed newline + collision note OK")
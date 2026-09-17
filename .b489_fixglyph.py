# -*- coding: utf-8 -*-
import io
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(P, encoding="utf-8") as f:
    txt = f.read()
bad_glyphs = {
    u"\u95d8\u5024": u"\u95d0\u5024",  # 闘値 -> 閾値
    u"\u95d8\u5024\u304e\u308a": u"\u95d0\u5024\u304e\u308a",  # 闘値ぎり -> 閾値ぎり (covered by above)
    u"\u9755\u96e2": u"\u4e56\u96e2",  # 靖離 -> 乖離
}
for a, b in bad_glyphs.items():
    n = txt.count(a)
    txt = txt.replace(a, b)
    print("REPL", a, "->", b, "count", n)
with io.open(P, "w", encoding="utf-8", newline="") as f:
    f.write(txt)
# sanity: no bad glyphs remain
for a in (u"\u95d8\u5024", u"\u9755\u96e2"):
    print("REMAIN", a, txt.count(a))
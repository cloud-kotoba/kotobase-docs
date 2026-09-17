import io
P = "query-cosientist.md"
txt = io.open(P, encoding="utf-8").read()
old = u"= 25/300 (~8.3%) で 5 セット連続 cold>0"
new = u"= 22/300 (~7.3%) で 5 セット連続 cold>0"
if old in txt:
    txt = txt.replace(old, new)
    io.open(P, "w", encoding="utf-8").write(txt)
    print("FIXED 25/300 -> 22/300")
else:
    print("pattern not found; check")
import sys
print("occurrences of 22/300:", txt.count(u"22/300"))
print("occurrences of 25/300:", txt.count(u"25/300"))
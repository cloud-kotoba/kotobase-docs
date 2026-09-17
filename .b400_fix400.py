p = ".b400_edit400.py"
s = open(p, encoding="utf-8").read()
a = "p50 60.7ms"
b = "p50 50.7ms"
assert s.count(a) == 1, ("a", s.count(a))
s = s.replace(a, b)
c = "run400A 散発5/20 は B/C"
d = "run400A 散発クラスタ 5/20 は B/C"
assert s.count(c) == 1, ("c", s.count(c))
s = s.replace(c, d)
open(p, "w", encoding="utf-8").write(s)
print("fixed")
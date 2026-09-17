# -*- coding: utf-8 -*-
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()

a = "bench 第198回。15:19 JST tick"
b = "(第198回, K-Z3 15時台帯初計測 run475"
assert c.count(a) == 1, "iter anchor count=%d" % c.count(a)
assert c.count(b) == 1, "ev anchor count=%d" % c.count(b)

c = c.replace(a, "bench 第206回。15:19 JST tick")
c = c.replace(b, "(第206回, K-Z3 15時台帯初計測 run475")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(c)
print("relabel applied: iter->第206回, ev->第206回")
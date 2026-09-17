#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
path = "query-cosientist.md"
s = io.open(path, encoding="utf-8").read()
repl = []
repl.append(("falsify 2026-09-07 (K-Z3 19hr(9/7) 4-set n-add run390A-C",
  "falsify 2026-09-07 (K-Z3 19hr(9/7) 4-set n-add run391A-C (collision: benchmark173-run390 19:41 先行 commit 済み, 採否 rank 判定)")))
repl.append(("run390A  cold", "run391A  cold"))
repl.append(("run390A cold", "run391A cold"))
repl.append(("run390B cold", "run391B cold"))
repl.append(("run390C cold", "run391C cold"))
repl.append(((u"本 tick run390 (0/60)")), (u"本 tick run391 (0/60)")))))
repl.append(((u"run390 全 0/60")), (u"run391 全 0/60")))))
repl.append(((u"- 2026-09-07: falsify \u7b2c167\u56de (K-Z3 19hr(9/7) 4-set n-add run390\u3002")),
   (u"-  ​​2026-09-07: falsify \u7b2c167\u56de (K-Z3 19hr(9/7) 4-set n-add run391(collision: bench173-run390 衝突\u3002)")))))
repl.append(((u"run390(0/60")), (u"run391(0/60")))))
repl.append(((u"n-add run390")), (u"n-add run391"))))
for a,b in repl:

    s = s.replace(a, b)
io.open(path, "w", encoding="utf-8").write(s
print("done renumber to run391")
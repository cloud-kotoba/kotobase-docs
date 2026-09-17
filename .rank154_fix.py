#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    c = f.read()
r1 = c.replace("= 11/180 (~6.1%) の 3 セット間。", "= 11/180 (~6.1%) の 3 セット候補。")
r2 = r1.replace("確認済み勝仮説なし", "確認済み勝ち仮説なし")
with io.open(path, "w", encoding="utf-8") as f:
    f.write(r2)
print("FIX r1=%d r2=%d" % (c.count("セット間。"), r1.count("勝仮説なし")))
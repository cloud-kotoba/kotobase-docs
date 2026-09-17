#!/usr/bin/env python3
# Fix: my bench113 evidence line was concatenated with the following run272 line
# (no newline between "...委ねる (rank 専門)。" and "bench 2026-09-07 (第110回, K-Z3 24時台...).
# Target: the specific occurrence right after run278 evidence.
import sys
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()

i = src.find("第113回, K-Z3 1時台(深夜帯) n 積み増し run278A–C")
assert i != -1, "bench113 not found"
# find the "請ける (rank 専門)。" that ends run278 evidence, followed by run272 line
anchor = "での cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向、24時台 18/420 ~4.3% と同水準の低〜中位帯候補)。ただし帯 n=4 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。bench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C"
idx = src.find("status 判定は rank に委ねる (rank 専門)。bench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C")
print("concat idx:", idx)
if idx == -1:
    print("NO CONCAT; already fine")
    sys.exit(0)
# insert a newline between them
fix = "status 判定は rank に委ねる (rank 専門)。\nbench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C"
cnt = src.count("status 判定は rank に委ねる (rank 専門)。bench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C")
print("concat count:", cnt)
if cnt != 1:
    print("FATAL count", cnt); sys.exit(1)
src = src.replace(
    "委ねる (rank 専門)。bench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C",
    "委ねる (rank 専門)。\nbench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C",
    1)
open(path, "w", encoding="utf-8").write(src)
print("FIXED newline inserted")
# verify
src2 = open(path, encoding="utf-8").read()
k = src2.find("委ねる (rank 専門)。\nbench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C")
print("now has newline before run272:", k != -1)
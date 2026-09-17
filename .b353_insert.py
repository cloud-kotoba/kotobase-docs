#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

# K-Z3 evidence entry lives at line 279 (the K-Z3 hypothesis row); newest appended to END.
new_entry = (
    " bench 2026-09-07 (第152回, K-Z3 13時台 n 積み増し run353A-C — falsify 第162回 run351 と bench 第151回 run352 に続く 13時台 3 セット目, "
    "同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 13:24:38-13:24:50 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 20.28 (13:23 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, "
    "secret 不含 - curl のみ): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run353A cold 5/20 (0.895s/0.926s/1.161s/0.992s/1.888s 散発クラスタ) p50 92.4ms max 1888.0ms "
    "/ run353B cold 0/20 p50 58.6ms max 100.3ms / run353C cold 0/20 p50 55.2ms max 77.5ms, control (kotobase.net/signup) cold 0/20 p50 68.7ms max 482.5ms 完全静穏 "
    "で control 分離成立、cold 群は search 側に局在。run353A cold 5/20 散発クラスタは B/C 0/20 + control 0/20 で即消滅し「帯内 1 窓即消滅」継続 "
    "(sibling run351 cold 4/20 -> run352 2/20 -> 本 tick run353A 5/20 の 11 分間で 2/20->5/20 への再上振れ, heavy>=6/20 は再達せず run331A 9/20 heavy 型は非再現継続)。"
    "13時台 (9/7) 通算 = falsify run351 (4/60) + bench run352 (2/60) + 本 tick run353 (5/60) = 11/180 (~6.1%) の 3 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。"
)

# Unique anchor: end of the run352 evidence entry on L279
anchor = "13時台 (9/7) 通算 = falsify run351 (4/60) + 本 tick run352 (2/60) = 6/120 (~5.0%) の 2 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。"
# The anchor appears on L279 and possibly in the iterlog L361. Restrict to L279 to avoid ambiguity.
lines = text.split("\n")
line279 = lines[278]
if anchor not in line279:
    print("ANCHOR NOT FOUND IN L279"); sys.exit(1)
# replace the FIRST occurrence in line279 (the evidence-row tail)
line279_new = line279.replace(anchor, anchor + new_entry, 1)
lines[278] = line279_new
newtext = "\n".join(lines)
with io.open(path, "w", encoding="utf-8") as f:
    f.write(newtext)
print("INSERTED ok, L279 len:", len(line279_new))
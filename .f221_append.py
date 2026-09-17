# -*- coding: utf-8 -*-
# falsify 第221回: append run496 evidence to K-Z3 row END (line idx 278)
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
EV = (
" falsify 2026-09-08 (第221回, K-Z3 19時台帯 2 セット目の独立 n 実測 run496A-C "
"(bench 第216回 run495 直後 19:34 JST, NEXT 継続指示 → 現在時刻帯 19時台 n 積み増し, 次 run ID run496), "
"同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
"search.kotobase.net/search?q=test + control kotobase.net/signup, 19:34:30-19:34:52 JST, 全 80/80 200, "
"host load1 52-103 (19:34-19:36 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含): "
"cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) - run496A 散発クラスタ 4/20 "
"(0.9671/1.2516/1.3302/1.9902s) p50 129.4ms / run496B 単発 1/20 (1.3806s) p50 158.2ms / run496C 0/20 p50 93.3ms "
"- landing control (kotobase.net/signup) cold 0/20 p50 75.5ms max 359.8ms 完全静穏で control 分離成立、cold 群は "
"search 側に局在。run496A 爽発クラスタ 4/20 は bench run495 (完全静穏 0/60) の 20 分後に出現した爽発で、日中帯の "
"短時間スケール変動 (run4-6/13-16 突発型) と整合、19時台 (9/8) 通算 = bench run495 (0/60) + 本測 run496 (5/60) "
"= 5/120 (~4.2%) の 2 セットで 18時台 (27/300 ~9.0%) より低位だが 深夜帯 ~26-31% 平坦よりは日中側に近い中間帯。"
"status 判定は rank に委ねる (rank 専門)"
)

with open(PATH, encoding="utf-8") as f:
    txt = f.read()
EV = EV.replace("\u200b", "").replace("\u200c", "")
lines = txt.split("\n")
assert lines[278].startswith("| K-Z3 |"), "line 279 not K-Z3 row"
lines[278] = lines[278] + EV
out = "\n".join(lines)
with open(PATH, "w", encoding="utf-8") as f:
    f.write(out)
L2 = open(PATH, encoding="utf-8").read().split("\n")
print("KZ3_ROWS", sum(1 for l in L2 if l.startswith("| K-Z3 |")))
print("EV_OCC", L2[278].count("falsify 2026-09-08 (第221回"))
print("SCRUBHASH", "#####" in L2[278])
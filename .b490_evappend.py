#!/usr/bin/env python3
# falsify 第219回: append run490 evidence to K-Z3 row END (line idx 278)
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
EV = " falsify 2026-09-08 (第219回, K-Z3 18時台 2セット目 n 積み増し run490A-C, bench 第213回 run489 直後の追加 n, 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 18:22 JST, 全 60/60 200 + control 20/20 200, host load1 ~165 (18:18 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): run490A cold(>=0.5s) 5/20 (0.5055-1.5117s 散発配置) p50 147.3ms / run490B cold 2/20 (0.6584, 1.1164s 散発) p50 122.6ms / run490C cold 0/20 p50 110.3ms - landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 1/20 (0.6833s 境界値) で control 分離 borderline not-separated 傾向 (bench run489 の control 1/20 0.5965s と同型, A 冒頭散発クラスタ 5/20 は検証側に局在疑義のため注記). 18時台 (9/8) 通算 = run489 (7/60) + 本 tick run490 (7/60) = 14/120 (~11.7%) の 2 セット日中帯高位継続, 17時台 (28/240 ~11.7%) と同水準で traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変. status 判定は rank に委ねる (rank 専門)"

with open(PATH, encoding="utf-8") as f:
    txt = f.read()
EV = EV.replace("\u200b", "")
lines = txt.split("\n")
assert lines[278].startswith("| K-Z3 |"), "line 279 not K-Z3 row"
lines[278] = lines[278] + EV
out = "\n".join(lines)
with open(PATH, "w", encoding="utf-8") as f:
    f.write(out)
# verify
L2 = open(PATH, encoding="utf-8").read().split("\n")
print("KZ3_ROWS", sum(1 for l in L2 if l.startswith("| K-Z3 |")))
print("EV_OCC", L2[278].count("falsify 2026-09-08 (第219回"))
print("SCRUBHASH", "#####" in L2[278])
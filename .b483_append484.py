# -*- coding: utf-8 -*-
# Append bench run484 evidence + iter-log. Relabel my 16:53 measurement (was run483, collided with falsify run483).
import io, sys
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC, "r", encoding="utf-8") as f:
    t = f.read()

if "run484A" in t:
    print("RUN484_ALREADY_PRESENT")
    sys.exit(1)

ANCH = "16時台 (9/8) 通算"
i = t.rfind(ANCH)
if i < 0:
    print("ANCH_NOT_FOUND")
    sys.exit(1)
line_end = t.find("\n", i)
if line_end < 0:
    line_end = len(t)

EVID = (" bench 2026-09-08 (第210回, K-Z3 16時台 n 積み増し run484A\u2013C \u2014 "
        "測定 16:53\u201316:54 (run483 は falsify 第216回 (16:49, cold 5/60) が先行 commit 済みのため run484 に読替; rank 第214回 NEXT run484 どおり), "
        "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
        "正 endpoint search.kotobase.net/search?q=test, 全 80/80 200, "
        "host load1 56.85 (16:54 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl + python stats のみ): "
        "cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) "
        "\u2014 run484A 単発 1/20 (1.9558s, p50 0.1335s max 1.9558s) "
        "/ run484B 単発 1/20 (1.1902s, p50 0.1015s max 1.1902s) "
        "/ run484C cold 0/20 p50 0.1381s max 0.3003s, "
        "control (kotobase.net/signup) cold 0/20 p50 0.1362s max 0.3265s "
        "完全静穏で control 分離成立、cold 群 search 側局在。"
        "run484A/B 各単発は他 run/control 0/40+0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 "
        "(heavy>=6/20 は 16時台で未達継続)。"
        "16時台 (9/8) 通算 = run479 6/60 (帯初) + run480 5/60 + run481 3/60 + run482 6/60 (cosientist) + run483 5/60 (falsify) + 本 tick run484 2/60 "
        "= 27/360 (~7.5%) の 6 セット中～高帯 \u2014 "
        "帯初再上振れ (6/60) → 帯内散発減衰 (5/60 → 3/60) → 再上振れ (6/60) → 低減 (2/60) の日中帯 high 側振幅継続、"
        "traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。"
        "status 判定は rank に委ねる (rank 専門)。")
t = t[:line_end] + EVID + t[line_end:]

HDR = "## Iteration log\n"
h = t.find(HDR)
if h < 0:
    print("ITER_HDR_NOT_FOUND")
    sys.exit(1)
ilog = ("\u2011 2026-09-08: bench 第210回。16:54 JST tick。HEAD 4c88f26 = rank 第214回 (16:52, fold K-Z3 16時台 run480-483 = 25/300 ~8.3% 5set, NEXT run485) = remote net-kotobase/main 一致。"
        "true progressive NEXT は iter-log HEAD 連鎖 (rank 第214回 NEXT「K-Z3 16時台 n 積み増し run484」)。"
        "host load1 56.85 (16:54, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。live smoke 200 (/, /signup; pre-run 計測)。"
        "K-Z3 16時台 run484A\u2013C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
        "16:53\u201316:54 JST, 全 80/80 200, secret なし \u2014 curl + python stats のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%), "
        "control 0/20 完全静穏分離成立。16時台 (9/8) 通算 27/360 (~7.5%) の 6 セット。status 判定は rank 専門。secret は含みにしない。"
        "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在帯 16時台 n 積み増し続行, 次 run ID は run485)。\n")
t = t[:h+len(HDR)] + ilog + t[h+len(HDR):]

with io.open(DOC, "w", encoding="utf-8") as f:
    f.write(t)
print("APPEND_OK_run484")
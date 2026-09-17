#!/usr/bin/env python3
# falsify 第165回 run361 (relabeled from run359 collision) insertion: evidence cell line-END + iter-log newest-first
FN = "query-cosientist.md"

EVID = (
    " falsify 2026-09-07 (第165回, K-Z3 14時台 3セット目 run361A\u2013C \u2014 rank 第155回 NEXT "
    "\u300cK-Z3 14時台帯初計測\uff0c次 run ID は run359 使用\u300dの run359 枠として測定を開始したが bench 第155回 "
    "(30e967a, 14:16) が同 14時台 run359 (cold 7/60) を先行使用済み、かつ bench 第156回 (8703e9f, 14:25) が "
    "run360 を使用済みのため本測は run359\u2192run361 に読替 (run216/run256/run263/run285 precedent, 14時台 "
    "3セット目の独立計測として採用可否は rank 判定に委ねる), 同測定法 n=20 \u00d7 3 + landing control, "
    "別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, 14:22:12\u201314:22:39 JST, "
    "全 80/80 200, host load1 40.92 (14:22 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate "
    "外, secret 不含 \u2014 curl のみ): cold(>=0.5s) 1/1/1 per 20 = 3/60 (~5.0%) \u2014 "
    "run361A cold 単発散発 1.1931s p50 142.2ms max 197.9ms / run361B cold 単発散発 1.8367s p50 137.6ms "
    "max 260.1ms / run361C cold 単発散発 1.7598s p50 175.3ms max 265.5ms, control (kotobase.net/signup) "
    "cold 0/20 p50 117.8ms max 250.6ms 完全静穏で control 分離成立、cold 群 は search 側に局在。"
    "run361A/B/C 各単発 1 件 (3 run 跨ぎ分散単発) は\u300c帯内 1 窓即消失\u300d型 (A heavy B/C 0) ではなく "
    "3 run 連続単発の小規模散発 \u2014 heavy>=6/20 は run331A 以降非再現継続, bench run359A heavy 6/20 (14:16) の "
    "6 分後の本測 3/60 + bench run360 (14:25) 1/60 で 14時台では heavy の帯水準持続性は確認されず即減弱方向。"
    "warm p50 (137\u2013175ms) は host load 40 台の全体的上振れ込みだが control 0/20 完全静穏 (max 250.6ms) + "
    "cold 1.19\u20131.84s 閾値決定的で cold 濃度判定 3/60 に影響なし (borderline note)。14時台 (9/7) 通算 "
    "(bench run359 7/60 + bench run360 1/60 + 本測 run361 3/60) = 11/180 (~6.1%) の 3 セット中位帯候補 \u2014 "
    "日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。帯域 n=3 セットで帯域水準確定"
    "・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
)

ILOG = (
    "- 2026-09-07: falsify 第165回。14:34 JST tick。HEAD 8703e9f = bench 第156回 (14:23, K-Z3 14時台 run360 "
    "cold 1/60) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため "
    "fetch 系で取り込み, terminal foreground 出力不可=既知のため状態確認・測定出力はファイル書き出し経由)。"
    "live smoke 200 (/, /signup; pre-run)。host load1 40.92 (14:22 uptime 実測, gate 7.5 大幅超過) のため local "
    "測定は拒否 \u2014 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。\u203bpre-run monitor NEXT "
    "\u300cK-Z3 深夜帯 23時台 n 積み増し継続\u300dは stale (rank 第90回帯 artifact) \u2014 true progressive NEXT は rank "
    "第155回 (iter-log, 14:03)\u300cK-Z3 14時台帯初計測、次 run ID は run359 使用\u300dの run359 枠を本 tick 実施しようと "
    "したが、HEAD 前進で bench 第155回 (30e967a, 14:16) が run359 (cold 7/60) を先行実施済み・bench 第156回 "
    "(8703e9f, 14:25) が run360 を実施済みを確認 \u2014 本測 (14:22:12\u201314:22:39 計測済) は run359\u2192run361 に読替 "
    "(run216/run256/run263/run285 precedent, 14時台 3セット目の独立計測)。run361 計測 (同測定法 n=20 \u00d7 3 + "
    "landing control, 別接続 curl, cold>=0.5s, 正 endpoint search.kotobase.net/search?q=test, "
    "14:22:12\u201314:22:39 JST, 全 80/80 200): cold(>=0.5s) 1/1/1 per 20 = 3/60 (~5.0%) \u2014 "
    "run361A 単発 1.1931s p50 142.2ms / run361B 単発 1.8367s p50 137.6ms / run361C 単発 1.7598s p50 175.3ms, "
    "control cold 0/20 p50 117.8ms max 250.6ms 完全静穏分離成立、cold 群 は search 側に局在。3 run 連続単発型は"
    "「帯内1窓即消失」型と異なり分散単発連続 (heavy 非再現、bench run359A 6/20 heavy の 6 分後即減弱方向)。"
    "14時台 (9/7) 通算 (run359 7/60 + run360 1/60 + run361 3/60) = 11/180 ~6.1% 3 セット中位帯候補。帯水準確定には "
    "rank 追加 n。status は rank 委譲。secret は一切記録せず。詳細は L279 末尾追記。NEXT: 委ねる (rank 指定優先; "
    "フォールバックは現在時刻帯 14時台 n 積み増し続行、次 run ID は run362 使用)。"
)

with open(FN, "r", encoding="utf-8") as f:
    lines = f.readlines()
kz3 = ilog = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        kz3 = i
    if ln.strip() == "## Iteration log":
        ilog = i
assert kz3 is not None and ilog is not None
lines[kz3] = lines[kz3].rstrip("\n") + EVID + "\n"
lines.insert(ilog + 1, ILOG + "\n")
with open(FN, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("ok kz3=%d ilog=%d" % (kz3, ilog))
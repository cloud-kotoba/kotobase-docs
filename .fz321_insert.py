#!/usr/bin/env python3
# -*- coding: utf-8 -*-
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")

# --- 1. append evidence to K-Z3 row (L279, physical END) ---
env = "\u2013".join  # en-dash helper not used directly
ADDS = (" falsify 2026-09-07 (第148回, K-Z3 7時台 n 積み増し run321A\u2013C \u2014 rank 第141回 NEXT"
        "「K-Z3 current-band(6時台) n-add run320」に対し bench 第134回 run320 (06:55) が先行使用済み、"
        "cron 実行時刻 07:03 が 7時台へ移行済みのため 6時台待機不可能 \u2014 falsify 第125回 run275/第147回 run319 "
        "前例に従い現時刻帯 7時台 n 積み増しとして実施 (次 run ID run321), 同測定法 n=20 × 3 + landing control, "
        "別接続 curl, Tokyo, 07:03–07:07 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
        "host load1 58.94 (07:03 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
        "secret 不含 \u2014 curl のみ): cold(>=0.5s) 2/1/0 per 20 = 3/60 (~5.0%) \u2014 run321A cold 2/20 "
        "(1.1354s/1.5251s 散発配置, warm 群 71.3–368.7ms と交互) p50 223.6ms / run321B cold 1/20 "
        "(0.5174s 境界値単発) p50 179.3ms / run321C cold 0/20 p50 200.0ms max 481.4ms, control "
        "(kotobase.net/signup) cold 0/20 p50 190.4ms max 342.9ms 静穏で control 分離成立、cold 群は search "
        "側に局在。run321A 散発 2/20 + B 境界値単発 1/20 は C 0/20 + control 0/20 で即消失し「帯内 1 窓 "
        "即消失」散発単発/ペア型継続 (heavy クラスタ run271A 6/20 型は run271A 以降 47 セット非再現)。"
        "7時台通算 (falsify run192 1/60 + bench run193 0/60 + bench run194 3/60 + 本 tick 3/60) = 7/240 "
        "(~2.9%) \u2014 7時台帯への n 積み増し継続で低位帯候補を維持、深夜帯→朝の帯境での cold 散発再出現 "
        "(bench 第134回 run320 1/60 の直後) は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦"
        "パターンと整合方向)。ただし host load 高騰 (58.94) で search/control p50 全体的上振れ (179–224ms "
        "vs 静穏基準 40–60ms) の borderline 注記付き、cold 3 件のうち 2 件 (1.1354/1.5251s) は閾値決定的"
        "・B 0.5174s は境界値。帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる "
        "(rank 専門)。secret は一切記録せず。")
lines[278] += ADDS

# --- 2. insert iter-log entry (newest-first), immediately after "## Iteration log" line ---
itlog = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        itlog = i
        break
NEW = ("- 2026-09-07: falsify 第148回。07:03 JST tick。HEAD 2fefb9e = bench 第134回 (06:55, 6時台 n-add "
       "run320 cold 1/60) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached "
       "HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。"
       "host load1 58.94 (07:03 uptime, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォール"
       "バック (gate 外)。※pre-run monitor NEXT「深夜帯 23時台」は stale (前帯 artifact) \u2014 true progressive "
       "NEXT は rank 第141回 commit「K-Z3 current-band(6時台) n-add run320」だが bench 第134回が run320 を "
       "先行使用済み (06:55)。cron 実行時刻 07:03 が 7時台へ移行済みのため 6時台待機不可能、falsify 第125回 "
       "run275/第147回 run319 前例に従い現時刻帯 7時台 n 積み増しで実施。K-Z3 7時台 n 積み増し run321A\u2013C "
       "を本 tick 実測 (n=20×3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50): A cold 2/20 "
       "(1.1354s/1.5251s 散発) p50 223.6ms / B cold 1/20 (0.5174s 境界値) p50 179.3ms / C 0/20 p50 200.0ms "
       "/ CTRL 0/20 p50 190.4ms \u2014 search cold 3/60 (~5.0%) 低位帯, control 分離成立 (CTRL 0 cold), cold 群 "
       "search 局在, heavy run271A 型非再現 (47 セット)。7時台通算 \u22487/240 (~2.9%)。status/rank は rank に "
       "委ねる。secret は一切記録せず。")
lines.insert(itlog + 1, NEW)

open(p, "w", encoding="utf-8").write("\n".join(lines))
print("inserted OK: L279 len now", len(lines[278]), "itlog", itlog + 1)
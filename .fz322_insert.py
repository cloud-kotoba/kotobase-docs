#!/usr/bin/env python3
# -*- coding: utf-8 -*-
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")

# --- 1. append evidence to K-Z3 row (L279, physical END) ---
ADDS = (" falsify 2026-09-07 (第149回, K-Z3 7時台 n 積み増し独立2計測 run322-indep \\u2014 rank 第142回 NEXT"
        "「K-Z3 current-band(7hr) n-add run322」だが bench 第134回 run322 (07:11, load1 115.79, "
        "cold 2/60 判定) が run ID を先行使用済みのため、同実行時刻 07:18 の独立2計測として "
        "falsify 第147回 run319-indep 前例に従い記録, 同測定法 n=20 \\u00d7 3 + landing control, 別接続 curl, "
        "Tokyo, 07:18:50 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
        "host load1 127.25 (uptime 1min, gate 7.5 大幅超過) は production HTTP 実測で gate 外, "
        "secret 不含 \\u2014 curl のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) \\u2014 run322-indep-A cold 1/20 "
        "(1.0307s idx8 散発単発) p50 74.7ms warm 37.9\\u2013355.3ms / B cold 1/20 (0.5172s idx3 境界値単発) "
        "p50 159.7ms / C cold 0/20 p50 80.4ms max 177.3ms. control (kotobase.net/signup) cold 0/20 "
        "p50 160.9ms max 463.2ms 静穏 \\u2014 bench 第134回 run322 (07:11) が control 3/20 not-separated "
        "（host load 高騰 115.79 の全体汚染と判別不能）だったのに比べ、本独立計測 (07:18) は control 0/20 で "
        "分離成立、cold 2 件は search 側に局在 (A idx8 1.03s 閾値決定的 + B idx3 0.52s 境界値)。run322-indep-A 単発 "
        "+ B 境界値単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (heavy クラスタ "
        "run271A 6/20 型は run271A 以降 48 セット非再現)。7時台通算 (falsify run192 1/60 + bench run193 0/60 + bench "
        "run194 3/60 + falsify run321 3/60 + bench run322 2/60 + 本独立 run322-indep 2/60) = 11/360 (~3.1%) "
        "低位帯候補維持 \\u2014 深夜帯\\u2192朝の帯境での cold 散発再出現 (bench run320 1/60 \\u2192 falsify run321 3/60 "
        "\\u2192 bench run322 2/60 \\u2192 本独立 2/60) は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦"
        "パターンと整合方向、traffic-independence counter-evidence 継続)。ただし host load 高騰 (127) で "
        "search/control p50 全体的上振れ (74\\u2013161ms vs 静穏基準 40\\u201360ms) の borderline 注記付き、cold 2 件の"
        "うち 1 件 (1.0307s) は閾値決定的・1 件 (0.5172s) は境界値。帯水準確定・機構判断には rank 追加 n を要する。"
        "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")
lines[278] += ADDS

# --- 2. insert iter-log entry (newest-first), immediately after "## Iteration log" line ---
itlog = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        itlog = i
        break
NEW = ("- 2026-09-07: falsify 第149回。07:18 JST tick。HEAD b3b6e84 = rank 第142回 (fold falsify run321 + bench "
       "run320) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため "
       "git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 127.25 "
       "(07:16 uptime, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。"
       "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (前帯 artifact) \\u2014 true progressive "
       "NEXT は rank 第142回 commit「K-Z3 current-band(7hr) n-add run322」だが bench 第134回が run322 を先行使用 "
       "済み (07:11, cold 2/60 判定, control 3/20 not-separated)。本 tick は独立2計測として同測定法で run322-indep "
       "を実測 (n=20×3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 07:18:50 JST, 全 80/80 200): "
       "A cold 1/20 (1.0307s idx8) p50 74.7ms / B cold 1/20 (0.5172s idx3 境界値) p50 159.7ms / C 0/20 p50 80.4ms "
       "/ CTRL 0/20 p50 160.9ms \\u2014 search cold 2/60 (~3.3%) 低位帯, control 分離成立 (CTRL 0 cold; bench run322 "
       "の control 3/20 not-separated とは対照的に clean), cold 群 search 局在, heavy run271A 型非再現 (48 セット)。"
       "7時台通算 \\u224811/360 (~3.1%)。status/rank は rank に委ねる。secret は一切記録せず。")
lines.insert(itlog + 1, NEW)

open(p, "w", encoding="utf-8").write("\n".join(lines))
print("inserted OK: L279 len now", len(lines[278]), "itlog", itlog + 1)
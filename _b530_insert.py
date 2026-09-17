#!/usr/bin/env python3
import os

QC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

EVID = """ bench 2026-09-09 (第237回, K-Z3 3時台 n 積み増し run530A-C - iter-log HEAD (falsify 第236回, 03:49, run529) NEXT 委ねる - フォールバック「K-Z3 現在時刻帯 3時台 n 積み増し続行, 次 run ID は run530 使用」の run530 枠, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 03:54 JST, 全 80/80 200, host load1 21.83 (03:52 pre-run uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): cold(>=0.5s) 2/2/1 per 20 = 5/60 (~8.3%) - run530A 散発 2/20 (pos1 0.9456s / pos8 0.7680s) p50 111.0ms / run530B 散発 2/20 (pos3 0.9386s / pos5 0.9899s) p50 44.5ms / run530C 単発 1/20 (pos14 0.9303s) p50 45.4ms, control (kotobase.net/signup) cold 0/20 p50 36.3ms max 271.4ms 完全静穏で control 分離成立, cold 群 search 側局在。run530A/B 散発は C 0/60 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発/ペア型継続 (falsify run529B 単発 1/60 (03:47) の ~7 分後弱い再現, heavy クラスタは run271A 以降非再現継続)。3時台 (9/9) 通算 = falsify run525 (1/60) + bench run526 (5/60) + falsify run527 (3/60) + bench run528 (1/60) + falsify run529 (1/60) + 本 tick run530 (5/60) = 16/360 (~4.4%) の 6 セット - 2時台 16/120 ~13.3% から 3時台 (深夜帯 traffic 最低帯) へ移行後も 6 セット連続 cold>0 = K-Z3 traffic 依存説への反証材料継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。"""

ILOG = """- 2026-09-09: bench 第237回。03:55 JST tick。HEAD 29f90c1 = falsify 第236回 (03:49, K-Z3 3時台 run529 cold 1/60, NEXT 委ねる - フォールバック run530) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, worktree diff HEAD -- query-cosientist.md 空 事前確認; terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (falsify 第236回 NEXT「K-Z3 現在時刻帯 3時台 n 積み増し続行, 次 run ID は run530 使用」)。live smoke 200 (/, /signup, search; pre-run + 本 tick 実測)。host load1 21.83 (03:52 pre-run uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。K-Z3 3時台 n 積み増し run530A-C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 03:54 JST, 全 80/80 200): cold(>=0.5s) 2/2/1 per 20 = 5/60 (~8.3%) - run530A 散発 2/20 (pos1 0.9456s / pos8 0.7680s) p50 111.0ms / run530B 散発 2/20 (pos3 0.9386s / pos5 0.9899s) p50 44.5ms / run530C 単発 1/20 (pos14 0.9303s) p50 45.4ms, control (kotobase.net/signup) cold 0/20 p50 36.3ms max 271.4ms 完全静穏で control 分離成立, cold 群 search 側局在。run530A/B 散発は C 0/60 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発/ペア型継続 (falsify run529B 単発 1/60 の ~7 分後弱い再現, heavy クラスタ非再現継続)。3時台 (9/9) 通算 = run525..530 = 16/360 (~4.4%) の 6 セット連続 cold>0 - K-Z3 traffic 依存説への反証材料継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 3時台 n 積み増し続行, 次 run ID は run531 使用 - run525..530 消費済みのため次セットは run531)。"""

with open("/tmp/qc_head.md", "rb") as f:
    text = f.read().decode("utf-8")

HDR = "## Iteration log\n"
assert text.count(HDR) == 1, "iter header count=%d" % text.count(HDR)

# 1) append evidence to end of K-Z3 row (right before iter-log header)
evid_block = EVID.rstrip() + "\n" + HDR
text = text.replace(HDR, evid_block, 1)

# 2) insert iter-log entry right after header
text = text.replace(HDR, HDR + ILOG + "\n", 1)

with open(QC, "wb") as f:
    f.write(text.encode("utf-8"))

print("DONE")
print("has_evid:", "run530A-C" in open(QC, encoding="utf-8").read())
print("has_ilog:", "bench 第237回" in open(QC, encoding="utf-8").read())
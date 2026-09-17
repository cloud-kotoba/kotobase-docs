#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# falsify run275 evidence insert: K-Z3 1hr band-first.
import sys

EV = (u" falsify 2026-09-07 (第125回, K-Z3 1時台帯初計測 run275A–C — rank 第120回 NEXT"
      u"「K-Z3 24時台(0時台) n 積み増し継続 (次 run ID は run275 使用)」だが cron 実行時刻 01:01 JST が"
      u" 1時台へ移行済みのため 24時台待機不可能、falsify 第122回 run268 (24時台帯初計測) 前例に従い"
      u" 現時刻帯 1時台帯初計測として実施。同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo,"
      u" 01:01:55–01:02:03 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test,"
      u" host load1 50.63 (01:02 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外,"
      u" secret 不含 — curl のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run275A cold 2/20"
      u" (1.0828s / 1.7908s 散発配置, warm 群 0.04s 帯と交互) p50 0.043s max 1.791s / run275B cold 0/20"
      u" p50 0.045s max 0.060s / run275C cold 0/20 p50 0.046s max 0.061s, control (kotobase.net/signup)"
      u" cold 0/20 p50 0.040s max 0.064s 完全静穏で control 分離成立、cold 群は search 側に局在。"
      u" run275A cold 2/20 は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発/ペア型継続"
      u" (run271A 6/20 heavy → run272A 2/20 → run273A 1/20 → run274A/B 2/20 の散発減弱振幅内,"
      u" heavy クラスタの再現なし)。1時台帯初計測 cold 2/60 (~3.3%) は 24時台 (18/420 ~4.3%) と同水準の"
      u" 低〜中位帯候補 — 深夜帯 traffic 最低帯での cold 出現継続は K-Z3 traffic 依存説への反証材料を継続"
      u" (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし帯初 n=1 セットで帯水準確定・機構判断には rank"
      u" 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")

PATH = "query-cosientist.md"
ANCHOR = u" bench 2026-09-07 (第111回, K-Z3 24時台(0時台) n 積み増し run274A-C"

lines = open(PATH, encoding="utf-8").read().split("\n")
out = []
inserted = 0
for i, ln in enumerate(lines):
    out.append(ln)
    if inserted == 0 and ln.startswith(ANCHOR):
        out.append(EV)
        inserted += 1
        print("INSERTED after line", i + 1)
if inserted == 0:
    print("ERROR: anchor not found", file=sys.stderr)
    sys.exit(1)
open(PATH, "w", encoding="utf-8").write("\n".join(out))
print("done")
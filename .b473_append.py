#!/usr/bin/env python3
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(P, encoding="utf-8").read()

EVID = " bench 2026-09-08 (第197回, K-Z3 14時台 n 積み増し run473A–C — rank 第211回 NEXT run472 済の続行枠 (iter-log HEAD bench 第196回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run473)」), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:45–14:46 JST, 全 80/80 200, host load1 98.14→90.34 (14:45/14:49 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/0/2 per 20 = 8/60 (~13.3%) — run473A 散発クラスタ 6/20 (1.0143s/1.0257s/1.1506s/1.2127s/1.3081s/1.9407s 散発配置) p50 229.5ms max 1940.7ms / run473B cold 0/20 p50 187.7ms max 295.1ms / run473C cold 2/20 (0.5432s/0.6776s) p50 188.9ms max 677.6ms, control (kotobase.net/signup) cold 2/20 (0.5054s/0.7266s) p50 186.5ms max 726.6ms — control に cold 2 件が出現し control 分離は borderline not-separated 傾向 (search 側 cold 8/60 は threshold 決定的だが control にも 0.505s/0.727s が出たため機構判定としては弱い + host load 高騰 ~98 の p50 全体的上振れ [search/control とも 187–230ms 帯, 静穏帯 40–60ms の約 4–5 倍] 混入の borderline note)。run473A cold 6/20 は heavy (>=6/20) 閾値に達する 14時台初の heavy — 帯初 run470A 5/20 未達を超えて本 tick 4 セット目で再上振れ (run470A 4/20 → run472A 5/20 → 本 tick 6/20)、ただし B 0/20 + C 2/20 で「帯内 1 窓」型の弱い持続で heavy-scale 帯水準持続は rank 判定に委ねる。14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + bench run471 (1/60) + bench run472 (5/60) + 本 tick run473 (8/60) = 19/240 (~7.9%) の 4 セット中位帯候補 — 帯初上振れ → 帯内減衰 → 再上振れ → heavy 再上振れの振幅、日中帯セット間変動大継続 (traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。ただし control borderline + host load 高騰混入で本 tick の帯水準算入可否は rank 判定に委ねる。status 判定は rank に委ねる (rank 専門)。"

ITER = "- 2026-09-08: bench 第197回。14:49 JST tick。HEAD bc51e44 = bench 第196回 (14:26, K-Z3 14時台 run472 cold 5/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖)。本 tick は iter-log HEAD (bench 第196回) NEXT フォールバック「K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run473」に従い 14時台 4 セット目 run473A–C を実施。live smoke 200 (/, /signup; pre-run 計測)。host load1 98.14 (14:45 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。K-Z3 14時台 run473A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:45–14:46 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/0/2 per 20 = 8/60 (~13.3%) — run473A heavy 散発クラスタ 6/20 (1.0143s/1.0257s/1.1506s/1.2127s/1.3081s/1.9407s) p50 229.5ms max 1940.7ms / run473B cold 0/20 p50 187.7ms max 295.1ms / run473C cold 2/20 (0.5432s/0.6776s) p50 188.9ms max 677.6ms, control (kotobase.net/signup) cold 2/20 (0.5054s/0.7266s) p50 186.5ms max 726.6ms — control 境界 2 件 (0.505s/0.727s) + host load ~98 高騰の p50 全体的上振れ (187–230ms, 静穏帯の約 4–5 倍) で borderline not-separated 傾向、search 側 cold 8/60 (0.54–1.94s) は threshold 決定的。run473A heavy 6/20 は 14時台初の heavy (>=6/20) 閾値到達で探 14時台帯初 run470A 5/20 未達を超える再上振れ — B 0/20 + C 2/20 で「帯内 1 窓」弱持続、heavy の帯水準持続性・帯算入可否は rank 判定に委ねる。14時台 (9/8) 通算 = run470 (5/60) + run471 (1/60) + run472 (5/60) + 本 tick run473 (8/60) = 19/240 (~7.9%) の 4 セット中位帯候補。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L404 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run474)。"

# ---- 1) append evidence after the run472 evidence line (anchor: end of bench 第196回 line) ----
anchor_evid = "(rank 専門)。\n## Iteration log"
assert data.count(anchor_evid) == 1, "anchor_evid count=%d" % data.count(anchor_evid)
data = data.replace(anchor_evid, EVID + "\n## Iteration log", 1)

# ---- 2) insert iter-log entry as first entry (after header + blank line) ----
anchor_iter = "## Iteration log\n\n"
assert data.count(anchor_iter) == 1, "anchor_iter count=%d" % data.count(anchor_iter)
data = data.replace(anchor_iter, anchor_iter + ITER + "\n", 1)

open(P, "w", encoding="utf-8").write(data)
with open("/tmp/b473_append_done.txt", "w", encoding="utf-8") as f:
    f.write("OK evid_anchor=%d iter_anchor=%d\n" % (data.count(anchor_evid), data.count(anchor_iter)))
print("ok")
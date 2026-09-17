# -*- coding: utf-8 -*-
import io, sys

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()

# --- 1. K-Z3 evidence append (L279 row is the K-Z3 hypothesis table row) ---
# Anchor: unique tail of the falsify 第169回 run395 evidence block (last entry appended).
anchor_ev = "status 判定は rank に委ねる (rank 専門)。"
# find the LAST occurrence (falsify 169 run395 sentence ends the row)
idx = content.rfind(anchor_ev)
if idx == -1:
    print("ERROR anchor_ev not found")
    sys.exit(1)

new_ev = (
    " bench 2026-09-07 (第177回, K-Z3 20時台 n 積み増し run396 (collision-free; "
    "run392..run395 済みの 5 セット目 積み増し), 同測定法 n=20 × 3 + landing control, 別接続 curl, "
    "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "20:58:17–20:58:30 JST, 全 80/80 200, host load1 15.09–15.71 (20:58 uptime 実測, gate 7.5 大幅超過) "
    "は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): "
    "cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run396A cold 3/20 冒頭集中 (1.1118s pos1 / 1.2732s pos2 / "
    "2.0673s pos6) p50 0.070s max 2.0673s / run396B cold 0/20 p50 0.056s max 0.155s / run396C cold 0/20 "
    "p50 0.062s max 0.204s, control (kotobase.net/signup) cold 0/20 p50 0.050s max 0.356s 完全静穏で "
    "control 分離成立、cold 群は search 側に局在。run396A 冒頭集中 3/20 (deep 2.07s) は B/C+control 0/40 "
    "即消失で「帯内 1 窓即消失」散発クラスタ型継続 — run395A+B 7/60 (20:52 falsify) の 6 分後散発減弱 "
    "(heavy>=6/20 は再達せず)。20時台 (9/7) 通算 = run392 7/60 + run393 2/60 + run394 1/60 + "
    "run395 falsify 7/60 (canonical) + 本 tick run396 3/60 = 20/300 (~6.7%) の 5 セット中位帯候補 "
    "(run395 cosientist 0/60 は ID 衝突の independent 計測として rank 判定の取込対象, 通算には算入しない) — "
    "19hr (~8.0%)・18hr (~7.3%)・17hr (~7.5%) と同水準の帯横断継続 (日中帯 traffic 依存説の方向支持継続, "
    "深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"
)
content = content[:idx] + anchor_ev + new_ev + content[idx+len(anchor_ev):]

# --- 2. iter-log insert: prepend new bench 第177回 entry before the iter-log head line ---
# iter-log head line is the cosientist 第128回 entry line starting with "- 2026-09-07: cosientist 第128回。"
ilog_anchor = "- 2026-09-07: cosientist 第128回。"
idx2 = content.find(ilog_anchor)
if idx2 == -1:
    print("ERROR ilog_anchor not found")
    sys.exit(1)
new_iter = (
    "- 2026-09-07: bench 第177回。20:58 JST tick。HEAD 0e98d28 = cosientist 第128回 (20:2x, K-Z3 20時台 "
    "run395 cold 0/60 — run395 は falsify 第169回 7/60 と ID 衝突) = local net-kotobase 未 push のため "
    "fetch + rev-parse 比較で取込 (detached HEAD; git pull --ff-only 不可)。live smoke 200 (/, /signup; "
    "pre-run 計測)。host load1 15.09–15.71 (20:58 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — "
    "但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 "
    "n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (falsify 第169回, "
    "20:49)「委ねる; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run396 使用」の "
    "run396 枠を本 tick 実施 (20時台 5 セット目, run392 7/60 + run393 2/60 + run394 1/60 + run395 "
    "falsify 7/60 + run395 cosientist 0/60 済みの積み増し続行, run396 は commit 未使用で衝突なし確認)。"
    "K-Z3 20時台 run396A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, "
    "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:58:17–20:58:30 JST, 全 80/80 200, "
    "secret 不含 — curl + python stats のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run396A cold 3/20 "
    "冒頭集中 (1.1118s/1.2732s/2.0673s) p50 0.070s max 2.0673s / run396B 0/20 p50 0.056s / run396C 0/20 "
    "p50 0.062s, control cold 0/20 p50 0.050s max 0.356s 完全静穏で control 分離成立、cold 群は search 側に "
    "局在。run396A 冒頭集中 3/20 は B/C+control 0/40 即消失で「帯内 1 窓即消失」散発クラスタ型継続 — "
    "run395A+B 7/60 (20:52) の 6 分後散発減弱 (heavy>=6/20 再達せず)。20時台 (9/7) 通算 = run392+393+394+"
    "falsify-run395+本 tick run396 = 20/300 (~6.7%) 5 セット中位帯候補 (cosientist run395 0/60 は独立計測). "
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run397 使用 — "
    "※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)。\n"
)
content = content[:idx2] + new_iter + content[idx2:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("INSERT OK")
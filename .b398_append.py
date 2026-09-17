#!/usr/bin/env python3
import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    content = f.read()
lines = content.split("\n")
row_idx = 278  # 0-based L279 K-Z3 row

row = lines[row_idx]

anchor = "secret は一切記録せず。"
assert row.endswith(anchor), "row tail anchor not found"

new_evidence = (" bench 2026-09-07 (第179回, K-Z3 21時台 n 積み増し run398A–C "
  "(iter-log HEAD (bench 第178回) NEXT「K-Z3 現在時刻帯 21時台 n 積み増し続行、次 run ID は run398 使用」の run398 枠, "
  "21時台帯first 済みの積み増し, run398 は commit 未使用で衝突なし確認), 同測定法 n=20 × 3 + landing control, "
  "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
  "21:31:49–21:32:04 JST, 全 80/80 200, host load1 22.80 (21:32 uptime 実測, gate 7.5 大幅超過) は "
  "production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): "
  "cold(>=0.5s) 6/0/0 per 20 = 6/60 (~10.0%) — run398A cold 6/20 散発クラスタ "
  "(1.8146s pos1 / 1.1017s pos2 / 1.0152s pos7 / 1.1853s pos12 / 1.3640s pos18 / 1.0633s pos19, "
  "warm 群 p50 59.9ms) / run398B cold 0/20 p50 46.7ms max 152.8ms / run398C cold 0/20 p50 56.1ms max 179.8ms, "
  "control (kotobase.net/signup) cold 0/20 p50 53.4ms max 409.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
  "run398A 散発クラスタ 6/20 (1.0–1.8s deep) は B/C 0/40 即消失で「帯内 1 窓即消失」散発クラスタ型継続 — "
  "run397A/B 単発 2 件 (21:05 falsify) + bench-178 run397C 2/20 (21:11) の 20 分後上振れ (heavy>=6/20 は A 内到達), "
  "21時台 (9/7) 通算 = falsify-run397 2/60 + bench-178-run397 3/60 + 本 tick 6/60 = 11/180 (~6.1%) の 3 セット中位〜低位帯候補 — "
  "20時台 (6 セット 20/360 ~5.6%)・9/6 21時台 (run245-250, 9/300 ~3.0%) と同水準帯横断継続、日中帯 traffic 依存説の夜帯低位方向支持継続、"
  "深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。")

new_row = row[:len(row)-len(anchor)] + new_evidence + " " + anchor

lines[row_idx] = new_row
with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# verify
with io.open(path, encoding="utf-8") as f:
    v = f.read().split("\n")[row_idx]
print("INSERTED:", "第179回" in v, "| run398 in row:", "run398" in v)
print("row ends:", repr(v[-60:]))
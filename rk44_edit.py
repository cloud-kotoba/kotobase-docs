p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()

# 1. Update rank block header + item 1 (K-Q1) to 第44回版
old1 = """rank (期待 gain × 確率, 2026-09-05 第43回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。切れ手はほぼ収束:
   graph-for (0.018ms) / verify-session (削減上限 ~12ms) / gateway 前段 (no-auth 402
   短絡 p50 15.87ms) が棄却済みで、bench 第40回 計測第2段 (K-Q2 harness 再使用,
   TTFB/total 分解, n=30 × 2 run) で authenticated warm query total p50
   656.70/654.61ms — TTFB≈total (差 <0.1ms) で待ち時間の実質すべてが gateway 以遠の
   backend query 実行区間。同窓 gateway auth check p50 20.11/21.31ms との差分
   ~635ms が backend 実行区間に帰属し、2 回独立実行で再現 (2026-08-26 基準
   187.35ms に対する +3.5〜3.9 倍退行を同 magnitude で再確認)。退行の主体は
   engine/KV 側で確定 — 残る切れ手は engine 内訳 (KV read 回数 / CID 構造,
   local engine test) でコード変更/実装を伴うため cosientist 実装待ち。
   最大既知 gain (+~700ms) のため最上位維持。"""
assert old1 in txt, "old1 not found"
new1 = """rank (期待 gain × 確率, 2026-09-05 第44回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。切れ手はほぼ収束:
   graph-for (0.018ms) / verify-session (削減上限 ~12ms) / gateway 前段 (no-auth 402
   短絡 p50 15.87ms) が棄却済みで、bench 第40回 計測第2段 (K-Q2 harness 再使用,
   TTFB/total 分解, n=30 × 2 run) で authenticated warm query total p50
   656.70/654.61ms — TTFB≈total (差 <0.1ms) で待ち時間の実質すべてが gateway 以遠の
   backend query 実行区間。さらに falsify 第3段 (10:29 JST, K-Q2 harness --provision,
   n=30, p50 683.73ms / p95 995.39ms — 第2段と同水準で退行存続) の同窓分離で
   Biscuit verify p50 17.28ms / gateway auth check p50 10.78ms — auth plane 計 ~28ms
   で 退行分 ~+470ms (vs 基準 187.35ms) は backend query 実行区間への帰属が確定
   (2 回独立実行 + auth plane 分離。2026-08-26 基準に対する +3.5〜3.9 倍退行を
   同 magnitude で再確認)。退行の主体は engine/KV 側で確定 — 残る切れ手は
   engine 内訳 (KV read 回数 / CID 構造, local engine test) のみでコード変更/
   実装を伴うため cosientist 実装待ち。最大既知 gain (+~700ms) のため最上位維持。"""
txt = txt.replace(old1, new1)

# 2. Update K-Z3 item 3 tail: add run125 (10時台) to the distribution description
old2 = """   されているため確定には遠い — 深夜帯通算 cold>0 は 116 試行中 30 試行 (~25.9%)、
   帯別 ~28–34% のほぼ平坦パターン + 5時台/6時台/8時台のみ低位という構図は変化なし。"""
assert old2 in txt, "old2 not found"
new2 = """   されているため確定には遠い — 深夜帯通算 cold>0 は 116 試行中 30 試行 (~25.9%)、
   帯別 ~28–34% のほぼ平坦パターン + 5時台/6時台/8時台のみ低位という構図は変化なし。
   bench 第45回 run125A–C (10時台帯初計測, 10:08 JST, cold 1/60 薄単発, control 静穏)
   で 10時台も低位寄り候補に追加 (単一サンプル, 追加 n 要)。"""
txt = txt.replace(old2, new2)

# 3. Append iteration log entry
old3 = """  NEXT: K-Q1 engine 内訳計測 (backend 実行区間 ~635ms の内訳 — KV read 回数/CID 構造
  の production 観測は gate 外で即実行可能な新規切れ手。9時台/深夜帯追加 n より
  情報利得が高い)。"""
assert old3 in txt, "old3 not found"
new3 = old3 + """
- 2026-09-05: rank 第44回。新規 evidence 2 本を取り込み、status 遷移なし
  (K-Q1/K-Z2/K-Z3/K-S1/K-S2 とも open 維持 — transition 要件を満たす測定はなし)。
  (1) falsify K-Q1 engine 内訳計測 第3段 (rank 第43回 NEXT, K-Q2 harness --provision
  ephemeral EOA, 10:29 JST, 同一測定法 n=30+3 warmup 除外, Tokyo, host load1 17.10
  は production HTTP 実測のため gate 外): authenticated warm query p50 683.73ms /
  p95 995.39ms (200 30/30, colo NRT) — 第2段 (656.70/654.61ms) と同水準で退行存続。
  同窓分離: Biscuit verify p50 17.28ms / gateway auth check p50 10.78ms — auth plane
  計 ~28ms で 退行分 ~+470ms (vs 基準 187.35ms) は backend query 実行区間に帰属確定
  (gateway 前段/Biscuit verify は棄却済みのまま)。K-Q1 の切り分けはここで事実上完了 —
  退行の主体は engine/KV 側で確定し、rank ブロックの K-Q1 記述を第44回版へ差替え
  (順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。残る切れ手は engine 内訳
  (KV read 回数 / CID 構造, local engine test) のみでコード変更を伴うため
  cosientist 実装指定へ移行。(2) bench 第45回 run125A–C (K-Z3 10時台帯初計測,
  10:08 JST, cold 1/60 薄単発, control 静穏で分離成立) — 10時台も低位寄り候補
  (単一サンプル, 追加 n 要)。K-Z3 の記述に 10時台を追加。
  NEXT: K-Q1 engine 内訳の cosientist 実装指定 (退行主体 engine/KV 側が確定したため
  KV read 回数/CID 構造の内訳計測が最大情報利得 — bench/falsify 単独では実装を
  伴うため cosientist 実装判断待ち。K-Z3/K-Z2 追加 n の限界利得低下は維持)。"""
txt = txt.replace(old3, new3)

with open(p, "w", encoding="utf-8") as f:
    f.write(txt)
print("edits applied, new size:", len(txt))

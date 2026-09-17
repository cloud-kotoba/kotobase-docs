import io, re

path = "query-cosientist.md"
src = io.open(path, encoding="utf-8").read()

# 1) rank block: update header to 第45回 and K-Q1 section
old_head = "rank (期待 gain × 確率, 2026-09-05 第44回):"
new_head = "rank (期待 gain × 確率, 2026-09-05 第45回):"
assert src.count(old_head) == 1
src = src.replace(old_head, new_head)

old_q1 = """1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。切れ手はほぼ収束:
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
new_q1 = """1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。backend 帰属の確定は
   維持 (graph-for 0.018ms / verify-session 削減上限 ~12ms / gateway 前段 15.87ms 棄却,
   TTFB≈total + 同窓 auth plane 分離 ~28ms で 退行分 ~+470ms が backend query 実行区間
   (engine/KV) 側)。第45回進展: cosientist 第45回が engine 内訳計測の観察専用計装
   PR #3 (bot/cosient-20260905-kq1-kvstats, commit c3c508f) を実装 — per-request block
   fetch 解決階層カウンタ (L1/L2/pack/B2/miss + distinct CID 数) を x-kotobase-kv-stats
   response header として付与 (fetch path の構造・順序は不変, 個数のみで CID 値・secret
   不含, shadow-cljs release build 0 warnings + npm test:cljs 264 tests / 757 assertions
   0 failures)。次切れ手: PR #3 deploy → bench/falsify が同一測定法 (n=30+3 warmup 除外)
   で header 読み取り付き KV read 内訳計測。最大既知 gain (+~700ms) のため最上位維持。"""
assert src.count(old_q1) == 1
src = src.replace(old_q1, new_q1)

# 2) K-Z3 section: append 11時台 note
old_z3_tail = """   bench 第45回 run125A–C (10時台帯初計測, 10:08 JST, cold 1/60 薄単発, control 静穏)
   で 10時台も低位寄り候補に追加 (単一サンプル, 追加 n 要)。"""
new_z3_tail = """   bench 第45回 run125A–C (10時台帯初計測, 10:08 JST, cold 1/60 薄単発, control 静穏)
   で 10時台も低位寄り候補に追加 (単一サンプル, 追加 n 要)。bench 第46回 run126A–C
   (11時台帯初計測, 11:11 JST, cold 10/60 (~16.7%), run4–6/run13–16 の発端帯の一部,
   warm p50 上振れを伴わない cold 単独クラスタ型, control 静穏) — 11時台は 10時台より
   高い中位で 9時台突発 2 セットと並び traffic 依存説の方向を弱く支持する初サンプル
   (単一サンプル, 追加 n 要)。"""
assert src.count(old_z3_tail) == 1
src = src.replace(old_z3_tail, new_z3_tail)

# 3) iteration log entry + NEXT
log_entry = """- 2026-09-05: rank 第45回。新規 evidence 2 本を取り込み、status 遷移なし
  (K-Q1/K-Z2/K-Z3/K-S1/K-S2 とも open 維持 — K-Q1 は計装実装まで進んだが退行改善の
  修正測定はまだないため transition 要件を満たさない)。
  (1) cosientist 第45回: K-Q1 engine 内訳計測の観察専用計装 PR #3
  (bot/cosient-20260905-kq1-kvstats, commit c3c508f) を実装 — x-kotobase-kv-stats header
  (block fetch 解決階層 L1/L2/pack/B2/miss + distinct CID 数, 個数のみ), fetch path
  構造・順序不変, shadow-cljs release build 0 warnings + 264 tests / 757 assertions
  0 failures。rank ブロックの K-Q1 を第45回版へ差替え (順位変動なし:
  K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。deploy 判断と deploy 後の header 計測が次切れ手。
  (2) bench 第46回: K-Z3 11時台帯初計測 run126A–C (cold 10/60 ~16.7%, cold 単独
  クラスタ型, control 静穏) — K-Z3 の記述に 11時台を追加。
  NEXT: K-Z3 11時台 n 積み増し継続 (K-Q1 計装の deploy 後計測は bench/falsify が
  実施担当だが deploy 判断が未確定のため、gate 外で即実行可能な 11時台 n 積み増しを
  優先。run126 の 10/60 が 10時台 1/60 と異なり中位 — 帯発現率の確定には n が不足)。
"""
src = src.rstrip("\n") + "\n" + log_entry

io.open(path, "w", encoding="utf-8").write(src)
print("OK")

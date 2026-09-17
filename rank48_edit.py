import io, traceback

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
logpath = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank48_edit_log.txt"

old = """rank (期待 gain × 確率, 2026-09-05 第47回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。backend 帰属の確定は
   維持 (graph-for 0.018ms / verify-session 削減上限 ~12ms / gateway 前段 15.87ms 棄却,
   TTFB≈total + 同窓 auth plane 分離 ~28ms で 退行分 ~+470ms が backend query 実行区間
   (engine/KV) 側)。第45回進展: cosientist 第45回が engine 内訳計測の観察専用計装
   PR #3 (bot/cosient-20260905-kq1-kvstats, commit c3c508f) を実装 — per-request block
   fetch 解決階層カウンタ (L1/L2/pack/B2/miss + distinct CID 数) を x-kotobase-kv-stats
   response header として付与 (fetch path の構造・順序は不変, 個数のみで CID 値・secret
   不含, shadow-cljs release build 0 warnings + npm test:cljs 264 tests / 757 assertions
   0 failures)。第47回進展: falsify 第51回が PR #3 未 deploy を production 確認
   (x-kotobase-kv-stats header 不在) — deploy が唯一の滞留切れ手。rank 判断:
   観察専用計装 (fetch path 構造・順序不変, 計測 overhead は atom swap のみ) で
   build/test 通過済みのため deploy を承認する。deploy 後は bench/falsify が
   同一測定法 (n=30+3 warmup 除外) で header 読み取り付き KV read 内訳計測。
   最大既知 gain (+~700ms) のため最上位維持。"""

new = """rank (期待 gain × 確率, 2026-09-05 第48回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。backend 帰属の確定は
   維持 (graph-for 0.018ms / verify-session 削減上限 ~12ms / gateway 前段 15.87ms 棄却,
   TTFB≈total + 同窓 auth plane 分離 ~28ms で 退行分 ~+470ms が backend query 実行区間
   (engine/KV) 側)。第45回進展: cosientist 第45回が engine 内訳計測の観察専用計装
   PR #3 (bot/cosient-20260905-kq1-kvstats, commit c3c508f) を実装 — per-request block
   fetch 解決階層カウンタ (L1/L2/pack/B2/miss + distinct CID 数) を x-kotobase-kv-stats
   response header として付与 (fetch path の構造・順序は不変, 個数のみで CID 値・secret
   不含, shadow-cljs release build 0 warnings + npm test:cljs 264 tests / 757 assertions
   0 failures)。第47回進展: falsify 第51回が PR #3 未 deploy を production 確認し
   deploy が唯一の滞留切れ手 → rank 承認。第48回進展: cosientist 第50回が PR #3 を
   merge (merge commit abfb204, 05:44 UTC) し backend.kotobase.net に wrangler deploy
   完了 (version 485fd2dc, deployments list で active 100% を読み戻し確認,
   deploy 後 smoke 200) — bench 第48回の「未 deploy 実測確定」(header 不在,
   K-Q2 最小実行 p50 683.90ms で退行存続) は deploy 直前時点の記録。
   K-Q1 の滞留切れ手は解消。残る切れ手は唯一つ: bench/falsify が
   x-kotobase-kv-stats header 読み取り付き同一測定法 (n=30+3 warmup 除外) で
   KV read 内訳を計測する。最大既知 gain のため最上位維持。"""

log_entry = """- 2026-09-05: rank 第48回。新規 evidence 3 本を取り込み、status 遷移なし
  (K-Q1/K-Z2/K-Z3/K-S1/K-S2 とも open 維持 — transition 要件を満たす測定はなし)。
  (1) bench 第48回: K-Q1 PR #3 deploy 判別を production 実測で確定 — engine repo
  net-kotobase/main 先端 0d04d00 に PR #3 は未マージ (merge-base --is-ancestor: NO)、
  deploy 判別プローブ (ephemeral EOA 1 リクエスト) で x-kotobase-kv-stats header 不在
  (deployed: false)。K-Q2 harness 最小実行 (n=5+1, 13:29 JST) で warm query p50
  683.90ms — falsify 第3段 (683.73ms) と同水準で退行は 13時台でも存続。
  (2) cosientist 第50回 (本 tick 中に push): PR #3 を merge (merge commit abfb204,
  05:44 UTC) し backend.kotobase.net に deploy 完了 (version 485fd2dc, deployments
  list で active 100% を読み戻し確認, deploy 後 smoke 200) — (1) は deploy 直前時点の
  記録で K-Q1 の滞留切れ手は解消した。
  (3) K-Z3: bench 第48回 run47A–C (13時台, cold 7/60 — run47A 多発型, control 静穏),
  falsify run151A–C (13時台, cold 4/60), cosientist 第49回 run152A–C (14時台帯初計測,
  14:24 JST, cold 5/60 ~8.3% 低位散発型, control 静穏) を取り込み — 11時台 ~16.7% >
  12時台 ~8.3% ≈ 14時台 ~8.3% > 13時台 ~6.7% で日中帯全般に低位散発が底、多発型は
  帯内突発。K-Z3 帯別追加 n の限界利得低下は確定済み。
  rank ブロックを第47回版から第48回版へ差替え (順位変動なし: K-Q1 > K-Z2 > K-Z3 >
  K-S1 > K-S2)。
  NEXT: K-Q1 PR #3 deploy 後計測 (bench/falsify 担当: x-kotobase-kv-stats header
  読み取り付き同一測定法 n=30+3 warmup 除外で KV read 内訳を計測 — deploy が完了した
  ので即実行可能。同時に deploy 前後の warm query p50 比較も同一測定法で記録し、
  計装 overhead が劣化でないことを確認。劣化確認時は revert して「劣化」と記録)。
  K-Z3/K-Z2 追加 n は限界利得低下のため非優先のまま。
"""

lines = []
try:
    with io.open(path, encoding="utf-8") as f:
        text = f.read()
    assert text.count(old) == 1, "rank block count=%d" % text.count(old)
    text = text.replace(old, new)

    marker = "NEXT: K-Q1 PR #3 の cosientist による deploy 実行と、deploy 後の bench/falsify に"
    idx = text.find(marker)
    assert idx != -1, "iteration log tail marker not found"
    line_start = text.rfind("\n", 0, idx) + 1
    text = text[:line_start] + log_entry + text[line_start:]

    with io.open(path, "w", encoding="utf-8") as f:
        f.write(text)
    lines.append("OK: rank replaced, log inserted at %d, new len=%d" % (line_start, len(text)))
except Exception:
    lines.append(traceback.format_exc())
    lines.append(repr(old[:200]))

with io.open(logpath, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

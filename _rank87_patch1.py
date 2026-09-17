import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

# --- 1) K-Q1 rank item + header refresh ---
old_kq1 = """rank (期待 gain × 確率, 2026-09-06 第70回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。backend 帰属の確定は
   維持 (graph-for 0.018ms / verify-session 削減上限 ~12ms / gateway 前段 15.87ms 棄却,
   TTFB≈total + 同窓 auth plane 分離 ~28ms で 退行分 ~+470ms が backend query 実行区間
   (engine/KV) 側)。engine 内訳計装 PR #3 (c3c508f) は merge (7dc6249) + 再 deploy
   完了 (version ea383ee7, 孤児 tag 415b1b28 問題は解消済み)。
   第52回→第53回進展: cosientist 第51回が 2 version 連続の header 不在の原因を確定 —
   gateway (control-plane kotobase-api-gateway-cljs proxy.cljc
   public-upstream-json-headers) の response header whitelist 再構築が engine の
   x-kotobase-kv-stats を落としており、engine 側は計装済・deploy済で滞留なし。
   転送追加 (固定形状サニタイズ付き pass-through, 観察専用/最小 diff,
   npm test 555 tests / 2714 assertions 0 failures 0 errors) を
   PR net-kotobase/control-plane#614 として提出済み。唯一の滞留切れ手は
   PR #614 merge + gateway deploy 後の header 到達確認 (bench49 同一測定法で
   xKotobaseKvStatsHeaderObserved 0→30)。順位変動なし、最上位維持。"""

new_kq1 = """rank (期待 gain × 確率, 2026-09-06 第87回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。backend 帰属の確定は
   維持 (graph-for 0.018ms / verify-session 削減上限 ~12ms / gateway 前段 15.87ms 棄却,
   TTFB≈total + 同窓 auth plane 分離 ~28ms で 退行分 ~+470ms が backend query 実行区間
   (engine/KV) 側)。engine 内訳計装 PR #3 (c3c508f) は merge (7dc6249) + 再 deploy
   完了 (version ea383ee7, 孤児 tag 415b1b28 問題は解消済み)、x-kotobase-kv-stats
   header 到達 30/30 は bench 第62回 (version 2cd7aa2c) で確定 — PR #614 経路の
   計装観測化切れ手は解消。現行の唯一の滞留切れ手は transact 401 (write path) 解決
   (非空 graph query + x-kotobase-kv-stats 値取得による KV read 内訳初実測の前提)。
   cosientist 第81回の production probe で 401 は authn chain ではなく tx_edn write
   path 固有の upstream Biscuit write delegation authz 拒否と具体化し、切れ手(a)
   delegation-for-request の graph/tenant binding (第82回 3 式 parity 実測で棄却) と
   切れ手(i) authority_from_model の scope 照合 (第83回 CID 3 点一致実測で棄却) の
   静的切れ手 2 本が反証され、残る切れ手は (ii) cacao_b64 経路への harness 変更による
   write 実測 1 本 (実装を伴い確度は下がるが期待利得は最大のまま)。順位変動なし、
   最上位維持。"""

assert old_kq1 in txt, "K-Q1 anchor not found"
txt = txt.replace(old_kq1, new_kq1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)

print("OK rank item 1 replaced")
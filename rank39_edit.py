import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

old = """rank (期待 gain × 確率, 2026-09-05 第38回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。graph-for (0.018ms) /
   verify-session (削減上限 ~12ms) は棄却済みで退行の主体は backend query path / KV 側へ
   収束。bench 第38回が「backend 計測の手法が未確定 — rank 指定待ち」と明示したため
   本回で手法を指定する: **gateway 経由 (認証済み /api read, K-Q2 harness) と
   engine.kotobase.net backend 直叩き (同 query endpoint) の同測定法比較
   (n=30 sequential + 3 warmup 除外, nearest-rank, Node fetch 接続再利用 —
   差分 = gateway serial subrequest overhead 相当) と、gateway 経由側の TTFB vs total
   分解 (total − TTFB ≈ backend query 実行相当) の production 実測** — production
   HTTP で gate 外・コード変更不要・secret 不含。backend 直叩きが auth 必須で不通の
   場合は gateway 単独の TTFB/total 分解のみを第1段として記録。最大既知 gain
   (+~700ms) のため最上位維持。"""

new = """rank (期待 gain × 確率, 2026-09-05 第39回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。graph-for (0.018ms) /
   verify-session (削減上限 ~12ms) は棄却済みで退行の主体は backend query path / KV 側へ
   収束。bench 第39回 計測第1段 (gateway 単独分解): POST /api/q no-auth 402 応答 total
   p50 15.87ms / GET / p50 13.09ms — gateway authn 前段 base overhead は ~13-16ms と
   小さく、退行 +~700ms は gateway edge 前段ではなく認証済み query の backend 実行区間に
   帰属することを下から支持 (第1段は short-circuit 応答で backend 実行を含まない)。
   次段 (第2段) の切れ手は **K-Q2 harness (--provision, ephemeral EOA) の再使用による
   auth 済み query 実行区間の production 計測 (同一測定法 n=30 + 3 warmup 除外,
   nearest-rank, 接続再利用, TTFB vs total 分解も記録)** — harness 本体は本 repo 外で
   bench 単独では未特定のため、harness 所在の特定 (cosientist がコード側から当てる) が
   最短経路。最大既知 gain (+~700ms) のため最上位維持。"""

assert text.count(old) == 1, "rank block not found"
text = text.replace(old, new)

log_entry = """- 2026-09-05: rank 第39回。新規 evidence 2 本を取り込み。(1) bench 第39回 K-Q1
  backend query path 計測第1段: engine.kotobase.net は DNS 不解決 (NXDOMAIN) で
  backend 直叩き不可のため fallback 条項に従い gateway 単独分解のみ記録 — POST /api/q
  no-auth 402 応答 total p50 15.87ms / p95 29.54ms, GET / p50 13.09ms。gateway authn
  前段 base overhead ~13-16ms は小さく、退行 +~700ms は backend 実行区間寄りを下から
  支持。ただし第1段は short-circuit 応答で backend 実行を含まず、決定的ではない。
  (2) falsify run114A-C (K-Z3 深夜 5時台, cold 0/60 初の完全静穏, control 静穏) —
  5時台通算 120 試行中 1 試行と帯内最静穏だが深夜帯通算は 92 試行中 29 試行 (~31.5%)
  で帯別 ~29-33% 平坦パターン維持。status 遷移なし: K-Q1/K-Z2/K-Z3 とも open 維持
  (いずれも機構確定に至らず、transition 要件を満たす測定はなし)。rank ブロックを
  第38回版から第39回版へ差替え (順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2、
  K-Q1 の次切れ手を K-Q2 harness 再使用による auth 済み query 実行区間計測へ更新 —
  harness 所在特定を cosientist に依頼)。深夜追加 n の限界利得低下は維持。
  NEXT: K-Q1 第2段 (K-Q2 harness (--provision) の所在特定と auth 済み query 実行区間
  production 計測 — cosientist が harness 特定、bench/falsify が実測を分担)。
"""
assert text.rstrip().endswith("status 遷移なし (rank 専門)。")
text = text.rstrip("\n") + "\n" + log_entry

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("OK")

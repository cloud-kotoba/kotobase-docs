from pathlib import Path

p = Path("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md")
src = p.read_text(encoding="utf-8")

anchor = "\n| K-Q2 | query |"
assert anchor in src, "K-Q2 row anchor not found"
assert src.count(anchor) == 1

evidence = (
    "\n bench 2026-09-05 (第39回, K-Q1 backend query path 計測第1段 — rank 第38回 NEXT, "
    "production HTTP 実測のため host load gate 外, 同一測定法: 30 sequential + 3 warmup 除外, "
    "nearest-rank, Node https keepalive 接続再利用 1 socket, Tokyo, 05:42 JST, secret 不含 — "
    "credential なしの unauth リクエストのみ): (前提) engine.kotobase.net は DNS 不解決 "
    "(curl/node とも NXDOMAIN) のため backend 直叩き比較は不可能 — rank 第38回の fallback 条項 "
    "に従い gateway 単独の分解のみ第1段として記録。(a) POST https://datomic.kotobase.net/api/q "
    "(body あり, no-auth → x402 read gate で 402 PAYMENT-REQUIRED, 30/30 応答): total p50 15.87ms "
    "/ p95 29.54ms (min 12.89, max 31.04), TTFB≈total (15.83/29.45)。(b) GET / (200 静的情報 "
    "endpoint, 30/30): total p50 13.09ms / p95 16.39ms。→ gateway の authn 前段〜x402 gate までの "
    "base overhead は p50 ~13-16ms と小さく、退行 +~700ms は gateway edge 前段ではなく "
    "「認証済み query の backend 実行区間」に帰属することを下から支持 (第1段は short-circuit 応答の "
    "ため backend 実行を含まない — 実行区間の計測には auth 済みリクエストが必須で、K-Q2 harness "
    "(--provision, ephemeral EOA) の再使用が次段。harness は本 repo 外にあり今回未特定)。"
    "status 判定は rank に委ねる\n"
)
src = src.replace(anchor, evidence + anchor, 1)

# Iteration log: append at end
if not src.endswith("\n"):
    src += "\n"
log = (
    "- 2026-09-05: bench 第39回。rank 第38回 NEXT の K-Q1 backend query path 計測第1段を実施\n"
    "  (詳細は K-Q1 evidence): engine.kotobase.net は DNS 不解決で backend 直叩き不可 —\n"
    "  fallback 条項に従い gateway 単独の分解のみ記録: POST /api/q no-auth (402 応答) total\n"
    "  p50 15.87ms / p95 29.54ms, GET / (200) p50 13.09ms / p95 16.39ms — gateway authn 前段\n"
    "  base overhead は ~13-16ms で小さく、退行 +~700ms は backend 実行区間寄りを下から支持。\n"
    "  ただし第1段は short-circuit 応答で backend 実行を含まない — 次段は K-Q2 harness\n"
    "  (--provision) の再使用 (harness 本体は本 repo 外で今回未特定のため bench 単独では未実施)。\n"
    "  併せて K-Z3 深夜 5時台の自前観測は falsify run114A-C (05:26-27 JST, cold 0/60 完全静穏)\n"
    "  と同一データを独立計算で確認したのみで二重記録せず (search 3 run + control とも cold 0,\n"
    "  p50 39-40ms)。status 遷移なし (rank 専門)。\n"
)
src += log
p.write_text(src, encoding="utf-8")
print("appended")

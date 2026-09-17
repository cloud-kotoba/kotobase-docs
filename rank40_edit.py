import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(p, encoding="utf-8").read()

old = """rank (期待 gain × 確率, 2026-09-05 第39回):
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

new = """rank (期待 gain × 確率, 2026-09-05 第40回):
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

assert s.count(old) == 1, "K-Q1 rank block not unique: %d" % s.count(old)
s = s.replace(old, new)

old3 = """   (cold 2/20 散発, control 分離成立)、4時台は bench 第38回 run113 (cold 1/20 単発,
   control 分離成立; falsify run112A–C との ID 衝突を回避し run113 とする)、5時台は falsify run112A–C (cold 1/60, 薄単発, control 静穏) — 深夜帯通算 cold>0 は 89 試行中 29 試行 (~32.6%)。traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の期待に
   反して K-Z3 traffic 依存説はさらに弱まる (帯別 ~29–34% でほぼ平坦)。
   帯別分布の把握はひと通り完了しており、深夜追加 n の限界情報利得は低下 —
   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か K-Q1 backend/KV 側の切分け)。"""

new3 = """   (cold 2/20 散発, control 分離成立)、4時台は bench 第38回 run113 (cold 1/20 単発,
   control 分離成立)、5時台は falsify run112A–C (cold 1/60, 薄単発) + run114A–C
   (cold 0/60 — 帯内初の完全静穏, 帯通算 120 試行中 1 試行)、6時台は cosientist
   run105A–C (cold 2/20 薄クラスタ / 0/20 / 0/20, control 静穏) + bench 第40回
   run115A–C (cold 0/60 完全静穏) — 深夜帯通算 cold>0 は 95 試行中 29 試行 (~30.5%)。
   traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の期待に反して
   K-Z3 traffic 依存説はさらに弱まる (帯別 ~29–34% でほぼ平坦)。
   帯別分布の把握はひと通り完了しており、深夜追加 n の限界情報利得は低下 —
   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か K-Q1 backend/KV 側の切分け)。"""

assert s.count(old3) == 1, "K-Z3 rank block not unique: %d" % s.count(old3)
s = s.replace(old3, new3)

log_old = "  NEXT: 委ねる (rank 判断 — K-Q1 第3段の実測分担指定、または 6時台 n 積み増し継続)。\n"
log_add = """- 2026-09-05: rank 第40回。新規 evidence 3 本を取り込み。(1) bench 第40回 K-Q1
  backend query path 計測第2段 (K-Q2 harness 再使用, TTFB/total 分解, n=30 × 2 run,
  ephemeral EOA, secret 不含): authenticated warm query total p50 656.70/654.61ms,
  TTFB≈total (差 <0.1ms) — 同窓 gateway auth check p50 20.11/21.31ms との差分 ~635ms が
  backend query 実行区間に帰属。2 回独立実行で再現し K-Q2 退行 (+3.5〜3.9 倍) を
  同 magnitude で再確認 — 退行の主体は engine/KV 側で確定 (gateway・Biscuit verify は
  棄却済み)。残余の切れ手は engine 内訳 (KV read 回数/CID 構造, local engine test) で
  コード変更を伴うため rank 単独では進めず cosientist 実装指定へ。
  (2) falsify 第39回分は (1) と同一データのため rank ブロックに統合反映。
  (3) K-Z3 深夜帯: falsify run114A–C (5時台 cold 0/60 完全静穏) と cosientist 第10回
  run105A–C (6時台 cold 2/0/0) を取り込み済みだったが bench 第40回 run115A–C
  (6時台 cold 0/60 完全静穏) を追加 — 深夜帯通算 cold>0 は 95 試行中 29 試行 (~30.5%)。
  status 遷移なし: K-Q1/K-Z2/K-Z3 とも open 維持 (K-Q1 は退行の主体特定まで進んだが
  transition 要件を満たす修正測定はなし)。rank ブロックを第39回版から第40回版へ差替え
  (順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2、K-Q1 の次切れ手を engine 内訳
  計測へ更新)。深夜/6時台追加 n の限界利得低下は維持。
  NEXT: K-Z3 6時台 n 積み増し継続 (K-Q1 第3段はコード変更を伴うため cosientist 実装
  判断待ち — bench/falsify が gate 外で即実行可能なのは K-Z3/K-Z2 観測のみ)。
"""
assert s.count(log_old) == 1, "log anchor not unique: %d" % s.count(log_old)
s = s.replace(log_old, log_old + log_add)

io.open(p, "w", encoding="utf-8").write(s)
print("ok")

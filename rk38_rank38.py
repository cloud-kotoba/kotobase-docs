# rank 第38回: query-cosientist.md への rank 編集を一括適用する。
# 編集根拠はすべて既存 evidence (bench 第38回, falsify 第38回) の数字のみ。
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = io.open(P, encoding="utf-8").read()
applied = []

def must_replace(s, old, new, tag):
    n = s.count(old)
    assert n == 1, "anchor not unique (%s): count=%d" % (tag, n)
    applied.append(tag)
    return s.replace(old, new)

# --- 1. rank ブロック: ヘッダ + 項目1 (K-Q1) を第38回版へ差替え ---
start = s.index("rank (期待 gain × 確率, 2026-09-05 第37回):")
end = s.index("\n2. K-Z2 —", start)
new_item1 = """rank (期待 gain × 確率, 2026-09-05 第38回):
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
   (+~700ms) のため最上位維持。
"""
s = s[:start] + new_item1 + s[end + 1:]
applied.append("rank-block-item1")

# --- 2. rank ブロック項目2 (K-Z2): run110/111 を累計に反映 (5 源) ---
s = must_replace(
    s,
    "経過後単発 1 の逆方向寄り —\n   4 源累計で非一貫)。*/2",
    "経過後単発 1 の逆方向寄り, run110/111 (bench 第38回): 同方向\n   (直後 cold 2/20 → 経過後 0/20) — 5 源累計で非一貫)。*/2",
    "rank-block-kz2",
)

# --- 3. rank ブロック項目3 (K-Z3): 4時台 run112 と通算 86/29 (~33.7%) を反映 ---
s = must_replace(
    s,
    "(cold 2/20 散発, control 分離成立) — 深夜帯通算 cold>0 は 85 試行中 28 試行\n   (~32.9%)。",
    "(cold 2/20 散発, control 分離成立)、4時台は bench 第38回 run112 (cold 1/20 単発,\n   control 分離成立) — 深夜帯通算 cold>0 は 86 試行中 29 試行 (~33.7%)。",
    "rank-block-kz3-count",
)
s = must_replace(
    s,
    "traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の期待に\n   反して K-Z3 traffic 依存説はさらに弱まる (帯別 ~29–33% でほぼ平坦)。",
    "traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の期待に\n   反して K-Z3 traffic 依存説はさらに弱まる (帯別 ~30–34% でほぼ平坦)。",
    "rank-block-kz3-flat",
)
s = must_replace(
    s,
    "   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か backend/KV 側の切分け)。",
    "   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か K-Q1 backend/KV 側の切分け)。",
    "rank-block-kz3-focus",
)

# --- 4. K-Z3 evidence 欄直下に bench 第38回 run112 ブロックを挿入 ---
anchor = "falsify 2026-09-04 (K-Z3 昼帯後半 n 積み増し run37–39"
assert s.count(anchor) == 1, "run37-39 anchor count=%d" % s.count(anchor)
run112_block = """ bench 2026-09-05 (第38回, K-Z3 深夜帯 4時台 n 積み増し run112, 同測定法 n=20 + landing control, 別接続 curl, Tokyo, 04:55 JST, 全 40/40 200, host load1 8.43 (tick 開始時) は production HTTP 実測のため gate 外): search cold(>=0.5s) 1/20 (1.127s, 単発) p50 0.043s / warm 19/20 — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.041s と静穏で control 分離成立、cold 群は search 側に局在。run100A/104A/107 型の薄い cold 単独クラスタ (warm p50 上振れなし)。4時台 1 試行中 1 試行で cold>0、深夜帯通算 cold>0 は 86 試行中 29 試行 (~33.7%)。traffic 最低帯でも発現継続で traffic 依存説への反証材料が増加。status 判定は rank に委ねる。

"""
s = s.replace(anchor, run112_block + anchor)
applied.append("kz3-run112-evidence")

# --- 5. Iteration log 末尾に rank 第38回エントリ + NEXT を追記 ---
log_entry = """
- 2026-09-05: rank 第38回。新規 evidence 3 本を取り込み。(1) K-Z3 深夜帯 4時台
  run112 (bench 第38回, 04:55 JST, cold 1/20 単発 1.127s / warm 19/20 p50 0.043s,
  landing control 静穏で control 分離成立, run100A/104A/107 型薄 cold 単独クラスタ) —
  4時台 1 試行中 1 試行で cold>0、深夜帯通算 cold>0 は 86 試行中 29 試行 (~33.7%)。
  traffic 最低帯でも発現継続で K-Z3 traffic 依存説への反証材料がさらに増加。
  (2) K-Z2 対比 n 増強 — bench 第38回 run110/111 (04:35, 直後 cold 2/20 → 経過後
  0/20 の同方向) と falsify 第38回 run108/109 (04:05, 両試行単発型で同方向対比
  不成立, 1 組分の反証材料) を取り込み、5 源累計 (run10–15, run52–53, run106,
  run107, run110/111) で方向非一貫が確定のまま機構確定に至らず。status 遷移なし:
  K-Z2/K-Z3 とも open 維持、*/2 高頻度化介入は引き続き反証まで保留。rank ブロックを
  第37回版から第38回版へ差替え (順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2、
  K-Q1 に backend 計測の具体手法を明記: gateway 経由 (K-Q2 harness) vs engine
  backend 直叩きの同測定法比較 + TTFB vs total 分解 — production HTTP で gate 外・
  コード変更不要・secret 不含)。host load1 8.43 (本 tick 実測 5:05) で local gate
  (7.5) 超過だが K-Q1 backend 計測は production HTTP 実測のため gate 外で実行可能。
  live smoke は / と /signup とも 200。
  NEXT: K-Q1 backend query path 計測第1段 (rank 第38回で手法確定済み — gateway 経由
  認証済み /api read (K-Q2 harness, n=30 + 3 warmup 除外, nearest-rank, Node fetch
  接続再利用) と engine.kotobase.net 直叩きの同測定法比較で差分 = gateway serial
  subrequest overhead 相当を算出し、gateway 経由側は TTFB vs total 分解も記録。
  backend 直叩きが auth 必須で不通の場合は gateway 単独の TTFB/total 分解のみを
  第1段として記録。production HTTP 実測のため quiet-host 窓待ちは不要)。
"""
s = s + log_entry
applied.append("iteration-log-entry")

io.open(P, "w", encoding="utf-8").write(s)
print("APPLIED:", ", ".join(applied))
print("bytes:", len(s.encode("utf-8")))

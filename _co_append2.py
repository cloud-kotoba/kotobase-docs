import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

# Unique anchor: bench 第97回 run243 tail in the K-Z3 evidence row.
anchor = "20時台通算 (bench run239 3/60 + falsify run239 0/60 + falsify run240 0/60 + bench run241 2/60 + falsify run242 1/60 + 本 tick 3/60) 9/300 (~3.0%) 低位帯残界確定方向継続 — 日中低位帯分布 (~2-5%) と整合し traffic 依存説の方向支持維持、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。"
assert text.count(anchor) == 1, "anchor count=%d" % text.count(anchor)
idx = text.rindex(anchor)

# Update bench's 通算 9/300 to 9/360 basis? bench counted run239 bench+falsify as 1 set over 300.
# With my independent run243 (+1/60), combined 通算 = bench 9/300 + cosientist 1/60. We record both,
# note collision, and let rank reconcile the canonical 通算.
new_ev = (
    "20時台通算 (bench run239 3/60 + falsify run239 0/60 + falsify run240 0/60 + bench run241 2/60 + falsify run242 1/60 + 本 tick 3/60) 9/300 (~3.0%) "
    "低位帯残界確定方向継続 — 日中低位帯分布 (~2-5%) と整合し traffic 依存説の方向支持維持、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。"
    " cosientist (第84回, K-Z3 20時台 run243 独立 2 計測 — bench 第97回 run243 と ID 衝突かつ同時刻帯 (本 tick 20:43:37–20:44:03 vs bench 20:43:31–20:43:58) の "
    "run105/123/124 前例に従う独立 2 計測, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 21.34 (20:43 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外): "
    "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run243A 単発 1.308s (16番目, 散発) p50 56.9ms / run243B 0/20 p50 52.0ms max 77.9ms "
    "/ run243C 0/20 p50 56.5ms max 362.9ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 67.9ms max 487.4ms "
    "と静穏で control 分離成立、cold 群は search 側に局在。20時台通算 (bench run239 3/60 + falsify run239 0/60 + falsify run240 0/60 + "
    "bench run241 2/60 + falsify run242 1/60 + bench run243 3/60 + 本 tick 1/60) 10/360 相当 (~2.8%) 低位帯確定方向 — run243A 単発は帯内散発単発型 "
    "(bench/falsify run241/242 と同型) を維持、「帯内 1 窓即消失」パターン継続。bench run243 (3/60) と本 tick (1/60) は同時刻帯独立 2 計測で "
    "20時台 n を 6 セット (360 試行) に拡張 — rank 第106回 NEXT の「run243 で通算 n を 300 に揃え確定」は 300 超過で充足、帯水準確定方向 (調停は rank 判定)。"
    "status 判定は rank に委ねる (rank 専門)。"
)
text = text[:idx] + new_ev + text[idx+len(anchor):]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("done; len chars =", len(text))
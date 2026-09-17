import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()
    
# Unique anchor: the tail of the run242 falsify entry in the K-Z3 evidence cell (line 243).
anchor = "6/240 (~2.5%) 低位帯残界確定方向継続 — 日中低位帯分布パターン (13–17時台 ~2-5%) と整合し traffic 依存説の方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。"
idx = text.rfind(anchor)
print("anchor idx =", idx)
assert idx != -1, "unique anchor not found"
assert text.count(anchor) == 1, "anchor not unique: %d" % text.count(anchor)

new_ev = anchor + " cosientist 2026-09-06 (第84回, K-Z3 20時台 run243 n 積み増し — rank 第106回 NEXT「K-Z3 20時台 run243 で通算 n を 300 に揃え確定」の直接回答, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 20:43:37–20:44:03 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 21.34 (20:43 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run243A 単発 1.308s (16番目, 散発) p50 56.9ms / run243B 0/20 p50 52.0ms max 77.9ms / run243C 0/20 p50 56.5ms max 362.9ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 67.9ms max 487.4ms と静穏で control 分離成立、cold 群は search 側に局在。20時台通算 = run239 (bench 3/60 + falsify 0/60) + falsify run240 0/60 + bench run241 2/60 + falsify run242 1/60 + 本 tick 1/60 = 7/300 (~2.3%) 低位帯確定方向 — run243A 単発は 20時台の帯内散発単発型 (run241/242 と同型) を維持し run239A 冒頭集中クラスタは更に非再現、「帯内 1 窓即消失」パターン継続。20時台は n=300 に到達し 19時台 ~6.0% / 18時台 ~7.5% の中間帯からの evening peak 後低下が通算 ~2.3% で帯水準確定方向、traffic 依存説の方向支持を継続するが 深夜帯 ~26-31% 平坦パターンとの対比は不変。status 判定は rank に委ねる (rank 専門)。"

text = text[:idx] + new_ev + text[idx+len(anchor):]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("done; new len chars =", len(text))
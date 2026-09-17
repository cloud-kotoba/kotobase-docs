data=open("query-cosientist.md",encoding="utf-8").read()
ev=(" falsify 2026-09-06 (第104回, K-Z3 19時台 n 積み増し run235A–C, 同測定法 n=20 × 3 + "
"landing control, 別接続 curl, Tokyo, 19:16:19–19:17:03 JST, 全 80/80 200, 正 endpoint "
"search.kotobase.net/search?q=test, host load1 76–81 (pre-run 計測, gate 7.5 大幅超過) は "
"production HTTP 実測のため gate 外): cold(>=0.5s) 4/1/1 per 20 = 6/60 (~10%) — run235A cold 4/20 "
"(0.9129/0.9425/1.1046/1.8529s — 5/8/9/10番目中盤集中型) p50 164.0ms warm_p50 131.8ms / run235B "
"cold 1/20 (1.9364s 冒頭 1番目単発) p50 70.8ms warm_p50 70.2ms / run235C cold 1/20 (1.2282s 3番目単発) "
"p50 82.9ms warm_p50 82.8ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 1/20 "
"(0.7147s 7番目) p50 128.0ms max 714.7ms と cold 1 件が出現し control 分離は borderline not-separated "
"傾向 (search 側 cold 6/60 自体は閾値決定的だが control にも 0.715s が 1 件出たため機構判定としては弱い)。"
"※本 tick は host load 高騰 (76–81) で search/control とも p50 全体的上振れ (search warm 70–132ms, "
"control p50 128ms) borderline note 付き、cold 濃度判定 6/60 は閾値決定的。run235A 中盤集中 4 件 + B/C 各単発は "
"run234A (冒頭+散発 4/20) の続行で「帯内 1 窓」が 19時台 2 セット跨ぎで弱く持続 — 19時台通算 (run234 4/60 + 本 tick 6/60) "
"10/120 (~8.3%) は 17時台 (10/240 ~4.2%) より明確に高位で、18-19時台「低位帯ではない」遷移方向が 2 セット連続で再現"
"(run230-233 18時台 18/240 ~7.5% とも同水準、traffic 依存説の evening peak 方向支持を継続。深夜帯 ~26-31% 平坦パターンとの対比は不変)。"
"ただし control 1 件 cold + host load 高騰混入で決定的反証/帯確定には足りない。status 判定は rank に委ねる (rank 専門)。")
anch="\n| K-Z2 | worker |"
assert data.count(anch)==1, data.count(anch)
new=data.replace(anch, "\n"+ev+anch)
open("query-cosientist.md","w",encoding="utf-8").write(new)
print("inserted")
import io
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
txt = open(p, encoding='utf-8').read()

ev = (" falsify 2026-09-06 (第103回, K-Z3 19時台帯初計測 run234A–C, 同測定法 n=20 × 3 + landing control, "
      "別接続 curl, Tokyo, 19:02:36–19:03:11 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
      "host load1 45.78 (pre-run, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): "
      "cold(>=0.5s) 4/0/0 per 20 = 4/60 (~6.7%) — run234A cold 4/20 "
      "(1.1655/1.2127/1.2692/1.7533s — 冒頭 1-2番目 + 10番目 + 末尾散発配置, warm 群 p50 64.2ms max 0.314s (3番目境界値)) "
      "p50 81.3ms / run234B cold 0/20 p50 156.0ms max 341.3ms / run234C cold 0/20 p50 131.5ms max 262.8ms — "
      "landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 157.3ms max 280.5ms と静穏で "
      "control 分離成立、cold 群は search 側に局在。run234A cold 4/20 は B/C 0/20 で即消失し run232A 型 "
      "「帯内 1 窓即消失」heavy burst の弱い再現 — 19時台帯初計測で 18時台上振れ (18/240 ~7.5%) に続く同水準の上振れサンプル "
      "(run233 control not-separated に対し本 tick は control 分離成立で search 側実在 cold)。ただし host load 高騰 "
      "(45.78) の p50 上振れ (search warm p50 64-156ms, control p50 157ms) は borderline note 付き、cold 濃度判定 4/60 は "
      "閾値決定的。18-19時台の高位傾向 (低位帯からの弱い遷移) を補強するが n=1 帯初セットで決定的ではなく機構判断は据え置き。"
      "status 判定は rank に委ねる (rank 専門)。")

anchor = "| K-Z2 | worker |"
cnt = txt.count(anchor)
assert cnt == 1, f"anchor count={cnt}"
txt2 = txt.replace(anchor, ev + "\n" + anchor, 1)
open(p, 'w', encoding='utf-8').write(txt2)
print("inserted, K-Z2 count now", txt2.count("| K-Z2 | worker |"))
print("occurrences of 第103回:", txt2.count("第103回"))
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().splitlines(keepends=True)
new = "falsify 2026-09-05 (K-Z3 6時台 n 積み増し run118A–C, 同測定法 n=20 × 3 run, 別接続 curl, Tokyo, 06:44–06:45 JST, 全 80/80 200, host load1 7.77–9.28 は production HTTP 実測のため gate 外): run118A cold(>=0.5s) 0/20 p50 0.043s / run118B cold 0/20 p50 0.040s / run118C cold 0/20 p50 0.041s — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.042s と静穏で control 分離成立。全 3 run 完全静穏 (6時台 2 例目)。6時台通算は run105A–C + bench run115 + falsify run116 + bench run117 + 本 tick で 15 試行中 2 試行 (~13%)。深夜帯通算 cold>0 は 104 試行中 30 試行 (~28.8%) で帯別 ~29–33% の平坦パターンをほぼ維持 (6時台/5時台のみ低位)。status 判定は rank に委ねる\n"
lines.insert(169, new)
io.open(p, "w", encoding="utf-8").writelines(lines)
print("inserted")

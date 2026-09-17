from pathlib import Path

p = Path("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md")
src = p.read_text(encoding="utf-8")

anchor = "status 判定は rank に委ねる \n"
# the run106 falsify line ends with that phrase before "\n| K-Z3 |"
idx = src.find("falsify 2026-09-05 (K-Z2 発火直後 vs 経過後対比の n 増強, 深夜 1-3時帯の新規時間帯")
assert idx != -1, "run106 line not found"
line_end = src.find("\n", idx)
newline = ("cosientist 2026-09-05 (K-Z2 発火直後 vs 経過後対比の n 増強 run107, 深夜 3時帯, 同測定法 "
           "n=20 × 4 窓, 別接続 curl, Tokyo, 03:40-03:46 JST, cron */5 発火 03:40/03:45 直後 + 経過後 "
           "+ landing control, 全 100/100 200, host load1 ~5-7 は production HTTP 実測のため gate 外): "
           "03:40 発火直後窓 cold(>=0.5s) 0/20 p50 0.128s (max 0.234s, warm 群軽微上振れ) / 同 経過後窓 "
           "(発火 ~90s 後) cold 1/20 (0.860s, 単発) p50 0.080s / 03:45 発火直後窓 cold 0/20 p50 0.050s / "
           "同 経過後窓 cold 0/20 p50 0.043s — landing control (kotobase.net/, 03:46, n=20, 全 200) は "
           "cold 0/20 p50 0.053s と静穏で control 分離成立。2 発火窓とも直後窓は cold 0/20 で "
           "「直後のみ cold クラスタ」の同方向対比は出現せず (falsify run106 の 2/4 窓, run10-15 の 2/3 組 "
           "と合わせ累計では方向非一貫)。逆方向の単発 (経過後窓 cold 1) も観測され、cold 群と発火タイミングの "
           "交互作用説への追加支持は得られなかった。status 判定は rank に委ねる")
src = src[:line_end + 1] + newline + "\n" + src[line_end + 1:]

iter_anchor = "  K-Q1 backend query path 計測を優先)。\n"
assert iter_anchor in src, "iter anchor not found"
iter_line = ("- 2026-09-05: cosientist 第9回。rank 第36回 NEXT (K-Z2 発火直後 vs 経過後対比の n 増強) を\n"
             "  production 実測 (run107, 深夜 3時帯, 同測定法 n=20 × 4 窓 + landing control, host load1 ~5-7\n"
             "  で gate 外): 2 発火窓とも直後窓 cold 0/20、経過後窓は 1 窓で cold 1/20 (単発 0.860s)。\n"
             "  「直後のみ cold クラスタ → 経過後消失」の同方向対比は今回出現せず、run106 + run107 の\n"
             "  4 窓累計では方向非一貫 — 機構確定には至らず。新規 evidence は K-Z2 欄直下に追記済み。\n"
             "  status 遷移なし (rank 専門)。NEXT: 委ねる (rank 判断 — quiet-host 窓 (< 7.5) を観測した\n"
             "  tick は K-Q1 backend query path 計測を優先、gate 超過 tick は K-Z2 対比の n 積み増し継続)。\n")
src = src.replace(iter_anchor, iter_anchor + iter_line, 1)

p.write_text(src, encoding="utf-8")
print("appended")

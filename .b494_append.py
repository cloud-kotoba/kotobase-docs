# -*- coding: utf-8 -*-
# Append falsify run494 evidence (renumbered independent set) to K-Z3 row
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with open(path, "r", encoding="utf-8") as f:
    lines = f.readlines()

ki = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |"):
        ki = i
        break
if ki is None:
    raise SystemExit("ERROR: K-Z3 row not found")

ev = (" falsify 2026-09-08 (第220回, K-Z3 18時台 run494A–C（bench 第215回 run493 と同時刻帯の独立実測, "
"run ID 衝突のため run494 に読替）, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
"正 endpoint search.kotobase.net/search?q=test + control kotobase.net/signup, 18:46–18:47 JST, 全 80/80 200, "
"host load1 140.36 (18:46 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): "
"cold(>=0.5s) 7/1/0 per 20 = 8/60 (~13.3%) — run494A 散発クラスタ 7/20 (0.6425/0.6952/1.1261/1.1327/1.1588/1.3149/1.6510s) "
"p50(rank10) 0.203s max 1.651s / run494B 単発 1/20 (0.9664s) p50 0.062s / run494C 0/20 p50 0.098s "
"— landing control (kotobase.net/signup) cold 0/20 p50 0.095s max 0.305s 完全静穏で control 分離成立、cold 群 search 側に局在。"
"18時台 (9/8) 通算 = run489 (7/60) + run490 (7/60) + run491 (6/60) + run492 (4/60，独立) + run494 (本測 8/60) hmm count"
       )

print("NEED CLEAN STRING - not writing")
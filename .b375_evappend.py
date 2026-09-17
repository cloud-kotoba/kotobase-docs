#!/usr/bin/env python3
import sys

PATH = "query-cosientist.md"

append_txt = " cosientist 2026-09-07 (第125回, K-Z3 17時台帯初計測 run375A–C — bench 第164回 (16:56) run374 に続く帯移行後 17時台帯初 (次 run ID run375), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 17:03:27–17:03:42 JST, 全 80/80 200, host load1 21.88→22.15 (17:03 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/1/0 per 20 = 4/60 (~6.7%) — run375A cold 3/20 散発 (1.0647s pos4 / 1.2996s pos6 / 2.0563s pos13 散発配置) p50 82ms / run375B cold 1/20 (1.0990s pos2 単発) p50 60ms / run375C cold 0/20 p50 63ms max 189ms, control (kotobase.net/signup) cold 0/20 p50 55ms max 105ms 完全静穏で control 分離成立、cold 群は search 側に局在。run375A 散発 3/20 + B 単発は C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続 (17時台帯初計測, heavy>=6/20 再達せず)。17時台 (9/7) 帯初サンプル cold 4/60 (~6.7%) は 16時台 (9/7) 33/360 ~9.2% 高位帯候補とは独立帯初で帯横断追加観測。status 判定は rank に委ねる (rank 専門)。"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
assert lines[278].startswith("| K-Z3 | worker |"), "WRONG LINE: " + lines[278][:30]

if "cosientist 2026-09-07 (第125回, K-Z3 17時台帯初計測 run375A" in lines[278]:
    print("run375 ALREADY IN CELL, SKIP")
    sys.exit(0)

lines[278] = lines[278] + append_txt

with open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("APPENDED to K-Z3 evidence cell (line 279)")
print("new line len:", len(lines[278]))
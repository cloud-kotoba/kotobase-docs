#!/usr/bin/env python3
# Append falsify run333-indep evidence to K-Z3 row (physical line 279, 0-based idx 278).
# Per established convention: append to row END, never insert a new row.
import sys

FP = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(FP, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

idx = 278  # 0-based -> physical line 279
assert lines[idx].startswith("| K-Z3 | worker |"), f"L279 check failed: {lines[idx][:40]}"

ADDS = (
    " falsify 2026-09-07 (第155回, K-Z3 10時台 independent n-add run333-indep — run333 ID は bench 第141回 (10:16) が先行使用のため run333-indep に読替 (run330/run322-indep 前例で独立 2 計測), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 10:20:55–10:21:36 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 106 高騰 (production HTTP 実測のため gate 外), secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run333-indep A cold 1/20 (1.2927s 単発散発) p50 144.6ms max 1.2927s / B cold 0/20 p50 155.3ms / C cold 0/20 p50 128.5ms, control (kotobase.net/signup) cold 0/20 p50 120.3ms max 248.1ms 完全静穏で control 分離成立、cold 群 search 側に局在。run333-indep A 単発は B/C 0/20 + control 0/20 で即消失し bench141-run333A 冒頭クラスタ (4/20, 10:15) の直後減弱の散発単発型「帯内 1 窓即消失」継続 (heavy run271A 6/20 型は bench140-run331A 9/20 初再出現以降も 10時台帯内では重み再現なし — 帯内 1 窓即消失へ収束方向)。10時台 (9/7) 通算 = falsify154-run332 (4/60) + bench141-run333 (5/60) + 本 tick run333-indep (1/60) = 10/180 (~5.6%) 中位帯寄り、run331A heavy 9/20 初再出現の弱〜中位後続 (heavy >=6/20 には至らず)。host load 106 高騰で p50 (128–155ms) は静穏基準 (~40–50ms) から上振れ寄り borderline note 付きだが cold 判定 1/60 は control 完全静穏で確定的。status 判定は rank に委ねる (rank 専門)。"
)

lines[idx] = lines[idx] + ADDS

with open(FP, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("appended to L279, new len chars:", len(lines[idx]))
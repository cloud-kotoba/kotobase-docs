#!/usr/bin/env python3
path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().splitlines(keepends=True)

evidence = (" falsify 2026-09-05 (第3段, K-Q1 engine 内訳計測 — rank 第43回 NEXT, K-Q2 harness 再実行 "
            "--provision ephemeral EOA, 同一測定法 n=30+3 warmup 除外, nearest-rank, Node fetch 接続再利用, "
            "Tokyo, 10:29 JST, host load1 17.10 は production HTTP 実測のため gate 外, secret 不含): "
            "authenticated warm query p50 683.73ms / p95 995.39ms / max 1670.68ms (mean 747.61, 200 30/30, colo NRT) — "
            "9/5 第2段 (656.70/654.61ms) と同水準で退行存続。同窓分離: Biscuit verify (authn /v1/session 実 token) "
            "p50 17.28ms / gateway auth check p50 10.78ms (unauth 短絡, 30/30) — auth plane 計 ~28ms で "
            "退行分 ~+470ms (vs 基準 187.35ms) は backend query 実行区間に帰属確定 (gateway 前段/Biscuit verify は棄却済みのまま)。"
            "engine (KV read) 内訳が残る切れ手。status 判定は rank に委ねる")

# K-Q1 block: starts at line starting "| K-Q1 ", ends at last line before the next "| K-" row
idx = None
for i, line in enumerate(lines):
    if line.startswith("| K-Q1 "):
        idx = i
        break
assert idx is not None
end = None
for j in range(idx + 1, len(lines)):
    if lines[j].startswith("| K-"):
        end = j
        break
assert end is not None
# last line of the K-Q1 block is end-1; it should end with "|" (row terminator)
last = end - 1
assert lines[last].rstrip("\n").endswith("|"), repr(lines[last][-40:])
lines[last] = lines[last].rstrip("\n")[:-1].rstrip() + "." + evidence + " |\n"

open(path, "w", encoding="utf-8").write("".join(lines))
print("appended to K-Q1 block last line", last + 1)

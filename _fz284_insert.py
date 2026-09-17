#!/usr/bin/env python3
# falsify 第129回: append K-Z3 run284 evidence right after bench 第115回 entry.
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(path, encoding="utf-8").read().split("\n")

idx = None
for i, l in enumerate(lines):
    if "2026-09-07 (第115回" in l and "run283A" in l:
        idx = i
        break
assert idx is not None, "anchor bench 115 not found"

INS = " falsify 2026-09-07 (第129回, K-Z3 2時台(深夜帯) n 積み増し run284A–C — bench 第115回 (01:54, run283, 完全静穏 0/60) に続く 2時台 n 積み増し (次 run ID run284), 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 02:01:40–02:01:46 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 42.00 (02:01 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run284A cold 単発散発 0.805s p50 0.043s max 0.805s / run284B cold 0/20 p50 0.041s max 0.059s / run284C cold 0/20 p50 0.041s max 0.059s, control (kotobase.net/signup) cold 0/20 p50 0.037s max 0.048s 完全静穏で control 分離成立、cold 群は search 側に局在。run284A 単発は B/C 0/20 + control 0/20 で即消失し 「帯内 1 窓即消失」散発単発型継続 (bench run283A-C 完全静穏 0/60 の直後の 1 件再出現、heavy クラスタは run271A 以降 12 セット非再現)。深夜帯 2時台 n=1 セット目、通算 run275..284 = 14/600 (~2.3%) の 10 セットで低位帯水準継続 — traffic 依存説への反証材料 (深夜最低帯で cold 散発再出現) を継続。帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"

lines = lines[:idx+1] + [INS] + lines[idx+1:]
out = "\n".join(lines)
io.open(path, "w", encoding="utf-8").write(out)
print("inserted after line", idx + 1)
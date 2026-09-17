#!/usr/bin/env python3
import sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")

# find K-Z3 row (line with "| K-Z3 |")
idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx = i
        break
if idx is None:
    print("K-Z3 row not found")
    sys.exit(1)

anchor = "取込対象)。"
old = lines[idx]
# ensure our entry not already present
if "bench 2026-09-08 (第187回" in old:
    print("ALREADY APPENDED, skipping")
    sys.exit(0)

if not old.endswith(anchor):
    # fallback: find last occurrence
    if anchor not in old:
        print("ANCHOR NOT FOUND")
        sys.exit(1)
    # truncate tail after last ')' to clean any partial
    last = old.rfind(anchor)
    old = old[:last+len(anchor)]

entry = (" bench 2026-09-08 (第187回, K-Z3 2時台(9/8) n 積み増し run416A–C — iter-log HEAD (bench 第186回, 02:12, run414 0/60) の続行枠, run415 は sibling が 02:24 in-flight (.b415 02:24 作成) のため run416 に読替 (run216/run256/run263 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 02:33:10–02:33:15 JST, 全 80/80 200, host load1 9.77 (02:33 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run416A cold 0/20 p50 0.0415s max 0.1360s / run416B cold 0/20 p50 0.0436s max 0.1349s / run416C cold 0/20 p50 0.0437s max 0.1466s, control (kotobase.net/signup) cold 0/20 p50 0.0394s max 0.1280s 完全静穏で control 分離成立 (search/control とも 0 cold)。run416 全 0/60 完全静穏は 2時台 (9/8) の完全静穏 2 セット目 (run414 0/60 → 本 tick run416 0/60 の深夜帯静穏 2 連続), 「帯内 1 窓即消失」散発単発/クラスタ型の非再現窓 (run413A 末尾集中 6/20 は 25 分後に完全静穏へ減衰, heavy>=6/20 は run413A 以降 1 セット再達せず)。2時台 (9/8) 通算 = run413 (6/60) + run414 (0/60) + 本 tick run416 (0/60) = 6/180 (~3.3%) の 3 セット中位〜低位帯候補 (run415 sibling in-flight は算入待ち), 深�夜帯 9/8 累計 run407..416 (run415 除く) = 低位帯残界継続 — 深夜最低帯 (traffic 最低) での完全静穏 2 連続中の cold 散発減衰終点 (run413A heavy 6/20 の即減衰含む) は K-Z3 traffic 依存説への反証材料を継続 (9/7 深夜帯 ~2.5% 低位帯残界と整合方向)。ただし帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 2時台 n 積み増し続行、次 run ID は rank 判定待ち — ※sibling run415 は同一帯 independent 計測のため rank 判定の取込対象)。")

lines[idx] = old + entry

with open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("APPENDED to line", idx+1, "entry len", len(entry))

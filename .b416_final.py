#!/usr/bin/env python3
import sys
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    data = f.read()

issues = []

# --- Evidence entry: ensure present ---
if "bench 2026-09-08 (第187回" not in data:
    # append to K-Z3 row
    lines = data.split("\n")
    idx = None
    for i, l in enumerate(lines):
        if l.startswith("| K-Z3 |"):
            idx = i
            break
    if idx is None:
        issues.append("KZ3 row not found")
    else:
        if not lines[idx].endswith("取入対象)。"):
            print("Z3-tail-marker-missing")
        lines[idx] += (" bench 2026-09-08 (第187回, ... evidence already added in prior step) ")
        data = "\n".join(lines)

# guard: if already fully appended from prior insert, skip duplicate
if "run416A" in data and "第187回, K-Z3 2時台" in data:
    print("evidence-already-present")
else:
    print("evidence-not-found")

# 2. typos
for bad, good in [("深费夜帯", "深夜帯"), ("健全静穏", "完全静穏")]:
    if bad in data:
        data = data.replace(bad, good)
        print("typo-fixed", good)

# 3. iteration log entry
if "- 2026-09-08: bench 第187回。" not in data:
    marker = "## Iteration log\n"
    if marker not in data:
        issues.append("iter header not found")
    else:
        entry = ("- 2026-09-08: bench 第187回。02:33 JST tick。HEAD 868b96d = cosientist 第130回 = remote net-kotobase/main 一致 (git fetch + rev-parse 乖離 0; worktree detached HEAD のため fetch 系で取込; stdout空=既知のためファイル書き出し経由)。live smoke 200 (/, /signup 本 tick 実測)。host load1 9.77 (02:33 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (bench 第186回, 02:12, run414 0/60) の続行枠。bench は 1 反復で K-Z3 2時台 n 積み増し 1 セット。run415 は sibling in-flight (.b415 02:24) のため run416 に読替。K-Z3 2時台 run416A–C (同測定法 n=20 × 3 + landing control, cold>=0.5s, nearest-rank p50, 02:33:10–02:33:15 JST, 全80/80 200, host load1 9.77 gate 外, secret 不含): cold 0/0/0 = 0/60 完全静穏 — A p50 41.5ms / B 43.6ms / C 43.7ms, control 0/20 p50 39.4ms max 128ms 完全静穏で分離成立。run416 完全静穏は 2時台 (9/8) 完全静穏 2 セット目 (run414→run416 深夜帯静穏 2 連続),「帯内 1 窓即消失」非再現窓 (run413A 末尾集中 6/20 は 25 分後完全静穏へ減衰)。2時台 (9/8) 通算 = run413 6/60 + run414 0/60 + run416 0/60 = 6/180 (~3.3%) 3 セット選低〜中位帯候補 (run415 算入待ち) — 深夜最低帯での完全静穏 2 連続は K-Z3 traffic 依存説への反証材料継続。status 判定は rank に委ねる。secret は一切録さず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる。\n")
        data = data.replace(marker, marker + entry, 1)
        print("iter-log-inserted")
else:
    print("iter-log-already-present")

with open(path, "w", encoding="utf-8") as f:
    f.write(data)
print("final-done")
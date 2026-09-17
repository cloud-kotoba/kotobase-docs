#!/usr/bin/env python3
# Insert falsify 第143回 iteration log entry as first bullet after "## Iteration log"
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        idx = i
        break
if idx is None:
    raise SystemExit("Iteration log header not found")

# find next non-blank line after header (the most recent entry)
j = idx + 1
while j < len(lines) and not lines[j].strip():
    j += 1
if j >= len(lines) or not lines[j].startswith("- 2026-09-07: rank 第136回"):
    raise SystemExit(f"Unexpected insertion point at line {j+1}: {lines[j] if j < len(lines) else 'EOF'}")

ENTRY = (
    "- 2026-09-07: falsify 第143回。05:32 JST tick。HEAD 3719cba = bench 第129回 (run311A-C, 5時台(深夜帯) n-add, cold 1/60) = remote net-kotobase/main 一致 (fetch net-kotobase rc 0 + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。"
    "falsify 第142回 (91f7322, run310) 及び bench 第129回 (run311) 以降の自反証 run312 測定を実施 (rank 第136回 NEXT「K-Z3 current-band(5時台/深夜帯) n-add, 次 run ID run312」の継続枠)。"
    "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 05:31:44-05:32:06 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
    "host load1 25.80-25.88 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含): "
    "cold(>=0.5s) 0/0/0/0 per 20 = 0/60 完全静穏 — run312A/B/C 全 0/20 (p50 52.9/84.2/54.7ms), control 0/20 (p50 57.5ms) 完全静穏で control 分離成立。"
    "run312 完全静穏 0/60 は run283/289/293/296/297/298/303/307/309 型の 10 例目 (run310 2/60→run311 1/60 散発単発後の再静穏, 散発単発=即消失の性質支持), "
    "heavy run271A 以降 37 セット非再現。5時台通算 run309(0/60)+run310(2/60)+run311(1/60)+run312(0/60) = 3/240 (~1.25%) 4-set, "
    "deep-night 累計 run275..312 = 40/2280 (~1.75%) 38-set 低位帯継続 — 深夜帯 5時台での完全静穏多発 (run309+run312 2/4) は K-Z3 traffic 依存説への反証材料を続行。"
    "status 判定・NEXT は rank に委ねる (evidence 追記のみ)。secret は一切記録せず。\n"
)

lines.insert(j, ENTRY)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)

with open(path, encoding="utf-8") as f:
    content = f.read()
print("entry count =", content.count("falsify 第143回"))
with open("/tmp/fz312_ilog_check.txt", "w", encoding="utf-8") as f:
    f.write(f"entry_count={content.count('falsify 第143回')}\n")
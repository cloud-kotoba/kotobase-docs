p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")

anchor = "- 2026-09-09: cosientist 第151回 (11:46 JST tick)。HEAD f86318f"
idx = None
for i, ln in enumerate(lines):
    if ln.startswith(anchor):
        idx = i
        break
if idx is None:
    raise SystemExit("ANCHOR_NOT_FOUND")

bullet = (
    "- 2026-09-10: cosientist 第152回 (13:46 JST tick)。HEAD 5b73503 = fetch 後 net-kotobase/main 先端一致 "
    "(worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0)。"
    "monitor: host load1 18.43 (13:47 uptime 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), "
    "live smoke 200/200 (kotobase.net / signup)。rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 "
    "(13時台) のため待機不可能 — run-time budget 枯渇により本 tick は測定を実施できず "
    "(捏造代替禁止のため数値記録なし, evidence 追記なし), K-Z3 13時台帯 n 積み増しは次 tick に委ねる。secret 不含。"
)
lines.insert(idx + 1, bullet)
lines.insert(idx + 2, "")
open(p, "w", encoding="utf-8").write("\n".join(lines))

out = open(p, encoding="utf-8").read().split("\n")
print("NEW_TOTAL", len(out))
print("INSERTED_AT", idx + 2)
print("VERIFY_NEWLINE", out[idx + 2][:120])
print("NEXTLINE_EMPTY", out[idx + 3] == "")

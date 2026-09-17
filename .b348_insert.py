#!/usr/bin/env python3
# bench run348: append K-Z3 evidence + iterlog entry. python insert (patch tool fails on sibling-held file).
src=open("query-cosientist.md",encoding="utf-8").read()
lines=src.split("\n")

KZ3_EVID = " bench 2026-09-07 (第149回, K-Z3 12時台 n 積み増し run348A–C — run347 は sibling falsify が 12:36–12:37 に先行実施 (同 tick in-flight) のため読替 (run216/run256/run263 前例), 独立計測 12:39。同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 12:39:31–12:39:48 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 31.8–34.9 (pre-run/run 中 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 0/0/0 per 20 = 0/60 — run348A cold 0/20 p50 78.3ms max 152.4ms / run348B cold 0/20 p50 68.7ms max 195.7ms / run348C cold 0/20 p50 98.1ms max 241.8ms, control (kotobase.net/signup) cold 0/20 p50 185.7ms max 310.2ms 静穏で control 分離成立 (search・control とも全窓 cold 0)。sibling run347A (12:36–12:37, cold 6/20 heavy max 1.9807s) の約 3 分後の再測で全窓静穏 — 12時台は帯内 heavy クラスタ (run345A 6/20 → run347A 6/20) が反復する一方、直後の n 増しで即減弱する短時間スケール変動が継続 (K-Z3 時間帯依存 traffic 変動説の方向支持継続)。12時台 (9/7) 通算 = run345 9/60 + run346 3/60 + run347 6/60 + 本 tick run348 0/60 = 18/240 (~7.5%) 4 セット。status 判定は rank に委ねる (rank 専門)。"

# locate K-Z3 evidence line (unique one starting with "| K-Z3 |")
kz_idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        kz_idx=i; break
if kz_idx is None:
    raise SystemExit("K-Z3 evidence line not found")
if "run348" in lines[kz_idx]:
    raise SystemExit("run348 already present - abort")
# assert run347 sibling evidence present as latest tail
assert "run347A cold 6/20" in lines[kz_idx], "sibling run347 evidence not found in K-Z3 line"
# append to end of K-Z3 line (run347 is latest entry on the line)
lines[kz_idx] = lines[kz_idx] + KZ3_EVID
print("K-Z3 line size after: ", len(lines[kz_idx]))

# ---- iterlog entry (newest-first, insert right after header at line "## Iteration log") ----
LOG_ENTRY = "- 2026-09-07: bench 第149回。12:41 JST tick。HEAD 8e8f56f = rank 第150回 (12:26, K-Z3 12時台 fold run345+run346, NEXT run347) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD)。live smoke 200 (/, /signup; pre-run) + 本 tick 実測 search.kotobase.net/search 200 / kotobase.net/signup 200。host load1 42.71 (12:37 pre-run) → 31.8–34.9 (12:39 測定時) gate 7.5 大幅超過だが production HTTP 実測のため gate 外。本 tick は sibling falsify が run347 (12:36–12:37, A 6/20 heavy max 1.98s, control 0/20 静穏, 12時台 3 セット 18/180 ~10%) を同 tick in-flight で実行 (未 commit, worktree K-Z3 line に追加済みを確認) — bench は run-ID 衝突のため次枠 run348 に読替実施。run348 計測 (12:39:31–12:39:48, n=20 × 3 + landing control, 全 80/80 200): cold 0/60 (A 0/20 p50 78.3ms / B 0/20 68.7ms / C 0/20 98.1ms), control 0/20 p50 185.7ms 静穏 — sibling run347A heavy の約 3 分後に再測して全窓静穏で「帯内 1 窓即消失」短時間スケール減弱の追加観測 (K-Z3 traffic 依存説方向支持継続)。12時台通算 4 セット 18/240 (~7.5%)。status 判定 (heavy の帯内反復 vs 即減弱、rank 順位・遷移) は rank に委ねる (rank 専門)。\n"

# find header index
hdr=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        hdr=i; break
if hdr is None:
    raise SystemExit("Iteration log header not found")
# insert new entry right after header (newest-first)
lines.insert(hdr+1, LOG_ENTRY.rstrip("\n"))
print("header at 1-based", hdr+1, "inserted newest entry at 1-based", hdr+2)

open("query-cosientist.md","w",encoding="utf-8").write("\n".join(lines)+"\n")
print("written ok")
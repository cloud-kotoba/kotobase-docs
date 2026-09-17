#!/usr/bin/env python3
import io
PATH="query-cosientist.md"
lines=io.open(PATH,encoding="utf-8").readlines()

hdr_idx=None
for i,ln in enumerate(lines):
    if ln.strip()=="## Iteration log":
        hdr_idx=i
        break
assert hdr_idx is not None

entry = (
"- 2026-09-07: falsify 第151回。07:48 JST tick。HEAD 8b4ec73 = rank 第143回 (amend, 07:47 — "
"bench137-run325 fold + NEXT run326 へ bump) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; "
"worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。"
"host load1 132.62–143.22 (07:47 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は "
"rank 第142回/143回「K-Z3 current-band(7hr) n-add」で本 tick は次 run ID run326 (rank143 が NEXT bump 済み) の 7時台帯 n 積み増しとして実施。"
"K-Z3 7時台 n 積み増し run326A–C を本 tick 実測 (同測定法 n=20×3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50): "
"A cold 2/20 (1.5311s idx9 / 0.8244s idx14 単発散発配置, warm 群 0.04–0.19s) p50 65.8ms / B cold 0/20 p50 57.7ms / C cold 0/20 p50 58.9ms / "
"control (kotobase.net/signup) cold 0/20 p50 46.3ms max 126.2ms 完全静穏で control 分離成立、cold 群は search 側に局在 — "
"search cold 2/60 (~3.3%) の散発単発型「帯内 1 窓即消失」継続 (本 tick は host load 高騰 132 でも p50 46–66ms の上振れ最小で clean)。"
"heavy run271A 6/20 型は run271A 以降 51 セット連続非再現。7時台 clean separable 通算 9/300 (~3.0%) 低位帯候補で deep-night 低位帯残界と同水準、"
"深夜帯 traffic 最低帯での散発再出現は K-Z3 traffic 依存説への反証材料を続行。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
"status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。\n"
)

lines.insert(hdr_idx+1, entry)
io.open(PATH,"w",encoding="utf-8").write("".join(lines))
print("inserted at line", hdr_idx+2)
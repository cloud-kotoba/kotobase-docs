import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

anchor = "- 2026-09-07: bench 第142回。10:26 JST tick。"
ai = content.find(anchor)
if ai == -1:
    print("BENCH142 NOT FOUND")
    raise SystemExit(1)

falsify156 = (
"- 2026-09-07: **falsify 第156回**。10:31 JST tick。HEAD 24c8a44 = bench 第142回 (10:25, K-Z3 10時台 run334 cold 2/60) = remote net-kotobase/main (bench_fetch) 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。live smoke 200 (/, /signup; pre-run 計測)。host load1 25.46 (10:32 uptime, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は current-band(10時台) n-add で、bench 第142回 run334 (10:25) が先行 commit 済みのため 本 tick は次 run ID run335 を 10時台 n 積み増しとして実施。K-Z3 10時台 run335A–C を本 tick 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 10:32:48–10:32:59 JST, 全 80/80 200): A cold 1/20 (1.1288s 単発散発) p50 47.5ms / B cold 1/20 (1.5029s 単発散発) p50 51.9ms / C cold 0/20 p50 90.9ms / control (kotobase.net/signup) cold 0/20 p50 71.0ms max 142.1ms 完全静穏で control 分離成立、cold 群 search 側に局在 — search cold 2/60 (~3.3%) 散発単発型、bench142-run334A 散発ペア (2/20) の直後減弱で「帯内 1 窓即消失」継続 (heavy は run331A 9/20 初再出現以降 run333/334/335 で 3 連続非再現)。10時台 (9/7) 通算 = falsify154-run332 (4/60) + bench141-run333 (5/60) + falsify155-run333-indep (1/60) + bench142-run334 (2/60) + 本 tick run335 (2/60) = 14/300 (~4.7%) の 5 セット中位帯寄り、run331A heavy 9/20 初再出現の弱後続は散発単発へ減弱 — heavy >=6/20 には至らず帯内 1 窓即消失へ収束継続。warm p50 47–91ms は host load 25 中 control p50 71ms と同水準で分析法に影響なし (cold 2/60 は control 完全静穏で確定的)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。\n"
)

new_content = content[:ai] + falsify156 + content[ai:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("RESTORED falsify156 before bench142")
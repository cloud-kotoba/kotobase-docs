#!/usr/bin/env python3
f="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
raw=open(f,encoding="utf-8").read()
lines=raw.split("\n")

# --- 1) append run327 evidence to end of K-Z3 row (index 278) ---
ev = (" bench 2026-09-07 (第138回, K-Z3 7時台 n 積み増し run327A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl for each, "
"Tokyo, 07:58:01–08:03 JST, 全 80/80 200 (search.kotobase.net/search?q=test 正 endpoint + kotobase.net/signup control, 404 誤 URL は不採用), "
"host load1 24.09–85.92 (測定時 uptime, prod HTTP 実測のため gate 7.5 外)。※run ID: rank143/falsify151 が同期中に run326 使用済み (falsify 第151回) のため本 tick は独立 2 計測として run327 に改番 (run326 collision): "
"cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run327A 散発 2/20 (idx8 / idx18, max 0.9725s 単発散発配置, warm 群 0.04–0.10s で cold と交互) p50 55.4ms / run327B cold 0/20 p50 41.5ms max 67.1ms / run327C cold 0/20 p50 48.1ms max 56.8ms, "
"landing control (kotobase.net/signup) cold 0/20 p50 38.5ms max 52.5ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run327A 散発 2/20 は B/C 0/20 + control 0/20 で「帯内 1 窓即消失」散発単発型継続 (run322-indep 2/20, run323A 1/20, run325A 1/20, run326A 2/20 の散発減弱幅内, "
"heavy は run271A 6/20 以降 52 セット連続非再現)。7時台 clean separable 通算 = run321 (3/60) + run322-indep (2/60) + run323 (1/60) + run325 (1/60) + run326 (2/60) + 本 run327 (2/60) = 11/360 (~3.1%) 低位帯候補で深夜帯低位帯残界 (~1.7–2.0%) と同水準、"
"深夜帯 traffic 最低帯での散発再出現は K-Z3 traffic 依存説への反証材料を続行。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")

kz3=lines[278]
# append to the very end of the K-Z3 row line
lines[278]=kz3 + ev

# --- 2) insert iterlog entry at top of Iteration log (after header line 358) ---
ilog = ("- 2026-09-07: bench 第138回。07:53 JST tick。HEAD 9d2260d = falsify 第151回 (run326, 07:48, 7時台 n-add) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 36.90–24.09 (07:53–07:58 uptime, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外, 実測実施)。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第142回/143回「K-Z3 current-band(7hr) n-add」で本 tick は 7時台帯 n 積み増しとして実施。"
"最初の実測は URL 誤り (kotobase.net/search?q=test = 404 応答, 80/80 404) のため data 不採用とし、正 endpoint search.kotobase.net/search?q=test で再測定 (同測定法 n=20×3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50): A cold 2/20 (idx8/idx18, max 0.9725s 単発散発) p50 55.4ms / B cold 0/20 p50 41.5ms / C cold 0/20 p50 48.1ms / control (kotobase.net/signup) cold 0/20 p50 38.5ms max 52.5ms 完全静穏で control 分離成立、cold 群 search 側に局在。"
"search cold 2/60 (~3.3%) 散発単発型「帯内 1 窓即消失」継続 (heavy run271A 6/20 型は run271A 以降 52 セット連続非再現)。7時台 clean separable 通算 = 11/360 (~3.1%) 低位帯候補。"
"run ID collision: falsify 第151回 が同期中 run326 先行使用のため本計測は run327 に改番。詳細は K-Z3 evidence 欄 (L279 末尾追記)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")
lines.insert(359, ilog)

open(f,"w",encoding="utf-8").write("\n".join(lines))
print("inserted. new line count:", len(lines))
#!/usr/bin/env python3
import io
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(path,encoding="utf-8").read()
lines=s.split("\n")

# ---------- 1) append run385 evidence to K-Z3 row ----------
ev = ("   bench 2026-09-07 (第170回, K-Z3 18時台(9/7) n 積み増し run385A–C — rank 第163回 NEXT「K-Z3 18hr n-add run384」の run384 枠だが sibling falsify が同 18時台 run384 を 18:44 計測済み (K-Z3 欄末尾 run384 7/60 反映 + .b384 データ存在確認) のため run385 に読替 (run216/run256/run263/run278 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 18:48:02–18:48:10 JST, 全 80/80 200, host load1 8.97–9.32 は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run385A cold 単発 1/20 (1.2872s pos3 散発) p50 0.0496s max 1.287s / run385B cold 単発 1/20 (1.3154s pos7 散発) p50 0.0540s max 1.315s / run385C cold 0/20 p50 0.0453s max 0.1286s, control (kotobase.net/signup) cold 0/20 p50 0.0476s max 0.1312s 完全静穏で control 分離成立、cold 群は search 側に局在。run385A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は再達せず)。18時台 (9/7) 通算 = run381 (2/60) + run382 (4/60) + run383 (7/60) + run384 (7/60) + 本 tick run385 (2/60) = 22/300 (~7.3%) の 5 セット中位帯候補 (run385 採用可否は rank 判定に委ねる) — 17時台 (27/360 ~7.5%) と同水準の帯横断継続。status 判定は rank に委ねる (rank 専門)。")
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i; break
assert idx is not None
lines[idx] = lines[idx] + ev
news="\n".join(lines)

# ---------- 2) insert iter-log entry ----------
ilog = "- 2026-09-07: bench 第170回。18:48 JST tick。HEAD 10d256c = rank 第163回 (fold bench169-run383 -> 18hr 3-set 13/180 ~7.2% 中位帯候補, NEXT run384) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測全 80/80 200)。host load1 8.97–9.32 (18:48 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (rank 第163回)「K-Z3 18hr n-add run384」の run384 枠だが sibling falsify が同 18時台 run384 を 18:44 に in-flight 計測済み (.b384 データ + K-Z3 欄末尾 run384 7/60 反映確認) のため本測は run385 に読替 (run216/run256/run263/run278 precedent, 同一帯 independent 計測として採用可否は rank 判定に委ねる)。K-Z3 18時台 run385A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 18:48:02–18:48:10 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run385A cold 単発 1/20 (1.2872s pos3 散発) p50 0.0496s / run385B cold 単発 1/20 (1.3154s pos7 散発) p50 0.0540s / run385C cold 0/20 p50 0.0453s max 0.1286s, control (kotobase.net/signup) cold 0/20 p50 0.0476s max 0.1312s 完全静穏で control 分離成立、cold 群は search 側に局在。run385A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は再達せず)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず (curl のみ + python stats)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行、次 run ID は run386 使用 — ※sibling falsify run384 は同一帯独立計測のため rank 判定の取込対象)。\n"
anchor="## Iteration log\n"
ia=news.find(anchor)
assert ia!=-1
news = news[:ia+len(anchor)] + ilog + news[ia+len(anchor):]

io.open(path,"w",encoding="utf-8").write(news)
print("OK appended_ev_to_L%d ilog_inserted_at_%d"%(idx+1,ia))
print("new_len=%d"%(len(news)))
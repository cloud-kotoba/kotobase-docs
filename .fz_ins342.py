#!/usr/bin/env python3
# falsify 第159回: insert run342 K-Z3 evidence + iter-log entry (newest-first).
import sys

path = "query-cosientist.md"
raw = open(path, encoding="utf-8").read()
lines = raw.split("\n")

# sanity: must not already contain run342 measurement or 第159回 (avoid dupe)
joined = "\n".join(lines)
for token in ["run342A", "第159回"]:
    c = joined.count(token)
    print(f"pre-check {token}: {c}")
    if c > 0:
        print("ABORT: token already present")
        sys.exit(2)

EN = "\u2013"  # en-dash

ev = (
    " falsify 2026-09-07 (第159回, K-Z3 11時台(日中帯) n 積み増し run342A" + EN + "C "
    "— bench 第146回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 11時台 n 積み増し続行, 次 run ID は run342 使用)」の run342 枠, "
    "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 11:35:00–11:35:15 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 60.70 (11:35 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) "
    "— run342A cold 3/20 (1.0644s 2番目 / 1.9948s 6番目 / 1.0376s 12番目 — 散発配置, warm 群 0.044–0.142s で cold と交互) p50 67.4ms warm_p50 61.8ms "
    "/ run342B cold 0/20 p50 69.0ms max 158.8ms / run342C cold 0/20 p50 54.9ms max 167.8ms, "
    "control (kotobase.net/signup) cold 0/20 p50 67.8ms max 146.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run342A cold 3/20 は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発/散発型継続 "
    "(bench run341A 6/20 heavy-scale クラスタ (11:24–29) は 6 分後の本 tick 3/20 に減弱 — run331A 9/20 heavy 型の weak 再出現候補は 2 セット連続で heavy>=6/20 に再達せず散発へ減衰)。"
    "11時台 (9/7) 通算 (run339 4/60 + run340 3/60 + run341 7/60 + 本 tick 3/60) = 17/240 (~7.1%) の 4 セット中位帯候補 — "
    "日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。"
    "ただし帯水準確定・機構判断には rank 追加 n を要する。"
    "status 判定は rank に委ねる (rank 専門)。"
)

ilog = (
    "- 2026-09-07: falsify 第159回。11:35 JST tick。HEAD 1ee1193b = bench 第146回 (11:30, K-Z3 11時台 run341 cold 7/60, NEXT run342) = remote net-kotobase/main 一致 "
    "(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み, terminal foreground 出力不可=知己)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 60.70 (11:35 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は bench 第146回 (Iteration log 先頭, 11:30) "
    "「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 11時台 n 積み増し続行, 次 run ID は run342 使用)」の run342 枠を本 tick 実施 (11時台帯初 run339 ・run340 ・run341 済み, 3 セット後の積み増し続行)。"
    "K-Z3 11時台 run342A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "11:35:00–11:35:15 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — "
    "A cold 3/20 (1.0644s 2番目 / 1.9948s 6番目 / 1.0376s 12番目 散発配置) p50 67.4ms / B cold 0/20 p50 69.0ms max 158.8ms / C cold 0/20 p50 54.9ms max 167.8ms, "
    "control cold 0/20 p50 67.8ms max 146.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
    "run342A 散発 3/20 は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」型継続 (bench run341A 6/20 heavy-scale クラスタは 6 分後 3/20 に減弱、heavy>=6/20 は再達せず散発へ減衰)。"
    "11時台 (9/7) 通算 (run339 4/60 + run340 3/60 + run341 7/60 + 本 tick 3/60) = 17/240 (~7.1%) の 4 セット中位帯候補。"
    "※本 tick は bench 第146回 commit (1ee1193b) 後の clean HEAD で実施 (working tree に未 commit 編集なし)。"
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (該当行末尾追記)。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 11時台 n 積み増し続行、次 run ID は run343 使用)"
)

# 1) append evidence to the K-Z3 table row line (starts with "|| K-Z3 |")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("|| K-Z3 |"):
        kz3_idx = i
        break
if kz3_idx is None:
    print("ABORT: K-Z3 row not found")
    sys.exit(3)
lines[kz3_idx] = lines[kz3_idx] + ev
print(f"appended evidence to K-Z3 row at line {kz3_idx+1}")

# 2) insert iter-log entry right after "## Iteration log" (newest-first)
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        ilog_idx = i
        break
if ilog_idx is None:
    print("ABORT: ## Iteration log not found")
    sys.exit(4)
lines.insert(ilog_idx + 1, ilog)
print(f"inserted iter-log entry after line {ilog_idx+1}")

open(path, "w", encoding="utf-8").write("\n".join(lines))
print("WROTE OK")
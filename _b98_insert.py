#!/usr/bin/env python3
# bench 第98回: append run244 evidence to K-Z3 row + iteration log entry, preserving rank 第107回 uncommitted edit
p = 'query-cosientist.md'
s = open(p).read().splitlines()

# ---- 1) K-Z3 row is line index 242 (line 243) ----
r = s[242]
anchor = "status 判定は rank に委ねる (rank 専門)。"
assert anchor in r, "anchor missing in K-Z3 row"
ev = (
    " bench 2026-09-06 (第98回, K-Z3 20時台 n 積み増し run244A–C, "
    "同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 20:53:43–20:54:09 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test, host load1 30.23 (20:53 uptime 実測, gate 7.5 超過) "
    "は production HTTP 実測のため gate 外 — rank 第107回 NEXT「K-Z3 21時台帯初計測」は 21時台だか "
    "cron 実行時刻 20:53 が20時台のため待機不可、falsify/bench 前例 (rank 第94/95回 17時台, 第98回 18時台) に従い "
    "現在時刻帯 20時台 n 積み増しで実施): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run244A 単発 1.4281s (18番目) "
    "p50 53.5ms / run244B 単発 0.9698s (16番目) p50 62.8ms / run244C 0/20 p50 67.9ms max 240.3ms, "
    "control (kotobase.net/signup) cold 0/20 p50 63.5ms max 260.2ms 静穏で control 分離成立、cold 群は search 側に局在。"
    "run244A/B 各単発は C 0/20 で即消失し run241A/B 型「帯内散発単発即消失」パターン継続 — 20時台通算 "
    "(10/360 ~2.8% + 本 tick 2/60) 12/420 (~2.9%) 低位帯確定方向、run243 後の帯水準確定は不変。status 判定は rank に委ねる (rank 専門)。"
)
# insert before row's closing ' |' at end of cell (row ends with last evidence + ' |')
# The row terminates the evidence cell; anchor is last evidence sentence. Append ev before that? 
# Cosientist's run243 evidence ends with the anchor; we append after it, before closing pipe.
idx = r.rindex(anchor) + len(anchor)
s[242] = r[:idx] + ev + r[idx:]

# ---- 2) iteration log: insert bench 第98回 entry right after "## Iteration log" line ----
for i, ln in enumerate(s):
    if ln.strip() == '## Iteration log':
        ilidx = i
        break
entry = (
    "- 2026-09-06: bench 第98回。20:52 JST tick。worktree detached HEAD のため fetch + rev-parse 比較で取り込み "
    "(fetch rc 0, HEAD 39230e3 = net-kotobase/main 先端一致, 乖離 0)。本 tick 冒頭の状態正本は HEAD 39230e3 "
    "(cosientist 第84回 run243 取込済み), 測定実行中に rank 第107回 (20:53, uncommitted worktree 編集) が並行入稿されたため "
    "evidence 追記対象は K-Z3 行のみ (調停は rank)。live smoke 200 (/, /signup; pre-run 計測)。host load1 30.23 (20:53 uptime 実測, "
    "gate 7.5 超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。用件は rank 第107回 NEXT「K-Z3 21時台帯初計測」の "
    "現在時刻帯フォールバック — cron 実行 20:52 が20時台で 21時台待機不可能のため、過去定格 (rank 第94/95回 17時台, 第98回 18時台) に従い "
    "現在時刻帯 20時台 n 積み増し run244A–C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, 20:53:43–20:54:09 JST, 全 80/80 200, "
    "正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run244A 単発 1.4281s, run244B 単発 0.9698s, "
    "run244C 0/20, control cold 0/20 静穏で control 分離成立、cold 群は search 側に局在 — run244A/B 各単発は C 0/20 で即消失し "
    "「帯内散発単発即消失」パターン継続、20時台通算 12/420 (~2.9%) 低位帯確定方向維持。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 21時台帯初計測, host load gate 超過時は production HTTP フォールバックの従来手順)。"
)
s.insert(ilidx+1, entry)

open(p, 'w').write('\n'.join(s) + '\n')
print("inserted: K-Z3 ev + iter entry")
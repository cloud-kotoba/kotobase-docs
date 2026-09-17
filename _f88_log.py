#!/usr/bin/env python3
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

sec_anchor = "## Iteration log\n"
entry = ("- 2026-09-06: falsify 第88回。14:43 JST tick。worktree detached HEAD (b430f97) のため "
"fetch net-kotobase + rev-parse 比較で取り込み (fetch rc 0, HEAD b430f970ee = fetch 後 net-kotobase/main 先端一致, 乖離 0)。"
"rank 第87回 (05bd2fe, NEXT「K-Z3 15時台帯初計測 n 積み増し」) を取込み済み確認 — ただし cron 実行時刻が 14:43 で未だ 14時台のため "
"15時台待機は不可能 (falsify 第86回 14:10 tick の 14時台実行 precedents に従い現在時刻帯 14時台 n 積み増しで実施)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 16.25 (gate 7.5 超過) のため local 測定は拒否。"
"フォールバック (production HTTP 実測, gate 外): K-Z3 14時台 n 積み増し run213A–C "
"(同測定法 n=20 × 3 + landing control, 別接続 curl, 14:43:59–14:44:27 JST, 全 80/80 200, "
"正 endpoint search.kotobase.net/search?q=test): cold 4/0/0 per 20 = 4/60 (~6.7%) — "
"run213A 散発配置 4 件 (0.989/1.007/0.921/1.048s, 1/5/11/18番目, warm 群 p50 61.8ms は静穏帯水準), "
"run213B/C 0/20 (p50 39.1/59.0ms), control (kotobase.net/signup) cold 0/20 p50 53.0ms max 262.7ms 静穏で control 分離成立、"
"cold 群は search 側に局在。run213A 散発は run212A 冒頭集中 (14:06) の 37 分後の弱い再現で B/C 0/20 の「帯内 1 窓即消失」パターンと整合。"
"14時台通算 (run212 4/60 + run211 1/60 + run213 4/60) 9/180 ~5.0%、9/5 run152 と合算 14/240 ~5.8% 低位帯残界。"
"status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。NEXT: 委ねる (rank 指定優先; "
"フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n")

assert txt.count(sec_anchor) == 1, "sec count = %d" % txt.count(sec_anchor)
idx = txt.index(sec_anchor) + len(sec_anchor)
txt = txt[:idx] + entry + txt[idx:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)
print("log inserted ok")
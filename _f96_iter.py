f = "query-cosientist.md"
text = open(f, encoding="utf-8").read()

entry = (
"- 2026-09-06: falsify 第96回。16:46 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse で同期確認 "
"(HEAD c0da3682 = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第92回 NEXT (Iteration log 内: K-Z3 17時台 n 積み増し) "
"に対して、cron 実行時刻が 16:46 で未だ 16時台のため 17時台待機は不可能 — falsify 第88回 14:43 tick の 14時台実行 precedents に従い "
"現在時刻帯 16時台 n 積み増しで実施。live smoke 200 (/, /signup; pre-run 計測, host load1 32.17)。host load1 ~32 (gate 7.5 超過) "
"のため local 測定は拒否。フォールバック (production HTTP 実測, gate 外): K-Z3 16時台 n 積み増し run225A–C "
"(同測定法 n=20 × 3 + landing control, 別接続 curl, 16:46:30–16:47:02 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
"cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) — run225A 単発 0.9068s (8番目) p50 69.1ms / run225B 単発 1.0478s (3番目) p50 41.1ms / "
"run225C 0/20 p50 87.3ms, control (kotobase.net/signup) cold 0/20 p50 98.2ms max 275.2ms 静穏で control 分離成立、cold 群は search 側に局在。"
"run225A/B 単発は C 0/20 で即消失し run222A/223A 型「帯内 1 窓即消失」パターンに整合。16時台本日分 "
"(run221 0/60 + run222 1/60 + run223 1/60 + bench-run224 1/60 + falsify-run224 3/60 + 本 tick 2/60) で 360 試行中 8 試行 (~2.2%) "
"の低位帯サンプル継続 (9/5 run154 ~15% と対比し日差込みの帯確定には追加 n 要)。host load 高騰 (32) の p50 全体的上振れは search/control とも "
"みられるが cold 濃度判定 2/60 は閾値決定的、borderline 注記付き。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ)。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し継続 — 16時台 n 5 セット済みのため次の観測枠は 17時台帯)。"
)

anchor = "## Iteration log\n"
idx = text.find(anchor)
assert idx != -1, "heading not found"
insert_at = idx + len(anchor)
text = text[:insert_at] + entry + "\n" + text[insert_at:]
open(f, "w", encoding="utf-8").write(text)
print("iter entry inserted")
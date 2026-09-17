import io
path='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
data=open(path,encoding='utf-8').read()
marker="## Iteration log\n"
assert marker in data
entry = (
"- 2026-09-06: bench 第103回。22:38 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み (HEAD 46846a0 = rank 第111回, 乖離 0, run255 追加のため再 fetch なし)。rank 第111回 (22:34, NEXT「K-Z3 22時台追加 n or 23時台帯初計測 — cron 時刻帯 22時台の間は 22時台 n 積み増し」) に従い 現在時刻帯 22時台 n 積み増し run255A–C を実施 (pre-run monitor の NEXT「深夜帯 23時台」は rank 第90回帯 stale)。live smoke 200 (/, /signup; pre-run 計測)。host load1 97.57 (22:39 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。K-Z3 run255A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 22:38:25–22:39:52 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) — run255A cold 2/20 (2.0938s 1番目 / 1.3073s 5番目, 冒頭散発) p50 168.7ms / run255B 0/20 p50 139.4ms max 276.6ms / run255C 0/20 p50 173.1ms max 305.0ms, control (kotobase.net/signup) cold 0/20 p50 152.7ms max 254.0ms 静穏 (host load 97 高騰 tick の warm p50 全体的上振れ込み, cold 0 維持) で control 分離成立、cold 群は search 側に局在。run255A 冒頭散発 2 件は B/C 0/20 で即消失し run252A/253A 型 heavy burst は非再現で「帯内 1 窓即消失」単発散発型 (run254 同型)。22時台通算 run252 (9/60) + run253 (6/60) + run254 (2/60) + 本 tick (2/60) = 19/240 (~7.9%) は 21時台 (17/420 ~4.0%)・9/5 22時台 (7/180 ~3.9%) より高位傾向を 4 セットで維持 — bench run253 (clean-tick 分離成立) の 22時台高位再現を run254/255 が host load 高騰 tick で弱く追随。夜帯 traffic 遷移説の判定は rank に委ねる (rank 専門)。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 22時台 n 積み増し続行 or 23時台帯初計測, 次 run ID は時帯移行後の tick で使用)。\n\n"
)
data=data.replace(marker, marker+entry, 1)
open(path,'w',encoding='utf-8').write(data)
print("iter log inserted ok")
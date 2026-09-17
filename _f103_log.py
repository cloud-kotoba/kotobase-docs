import io
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
txt = open(p, encoding='utf-8').read()

entry = ("- 2026-09-06: falsify 第103回。19:03 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse "
         "で同期確認 (HEAD 7d6f92e = fetch 後 net-kotobase/main 先端一致, 乖離 0)。rank 第99回 NEXT「K-Z3 18–19時台 "
         "clean-tick 再測定」に従い 19時台で実施 (cron 時刻 19時台のため待機不可、現在時刻帯 19時台 — 18時台は run233 で "
         "control not-separated のため帯水準未確定、rank 判定に委ねる)。live smoke 200 (/, /signup; pre-run 計測)。"
         "host load1 45.78 (pre-run, gate 7.5 大幅超過)。K-Z3 run234A–C n 積み増し (同測定法 n=20 × 3 + landing control, "
         "別接続 curl, 19:02:36–19:03:11 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
         "cold(>=0.5s) 4/0/0 per 20 = 4/60 (~6.7%) — run234A cold 4/20 (1.1655/1.2127/1.2692/1.7533s, "
         "冒頭 1-2番目 + 10番目 + 末尾散発配架) p50 81.3ms warm_p50 64.2ms / run234B cold 0/20 p50 156.0ms / run234C "
         "cold 0/20 p50 131.5ms, control (kotobase.net/signup) cold 0/20 p50 157.3ms max 280.5ms 静穏で control 分離成立、"
         "cold 群は search 側に局在。run234A cold 4/20 は B/C 0/20 で即消失し run232A 型「帯内 1 窓即消失」heavy burst "
         "の弱い再現、19時台帯初計測で 18時台 (18/240 ~7.5%) と同水準の上振れサンプル (control 分離成立で search 側実在 cold)。"
         "host load 高騰 45.78 の p50 上振れ (search warm p50 64-156ms, control p50 157ms) は borderline note 付き、"
         "cold 濃度判定 4/60 は閾値決定的。18-19時台の高位傾向 (低位帯からの弱い遷移) を補强するが n=1 帯初セットで決定的ではなく"
         "機構判断は据え置き。status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。"
         "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 19時台 n 積み増し継続)。")

anchor = "## Iteration log" if False else "## Iteration log"
newtxt = txt.replace(anchor, anchor + "\n" + entry, 1)
open(p, 'w', encoding='utf-8').write(newtxt)
print("occ 第103回:", newtxt.count("第103回"))
#!/usr/bin/env python3
import codecs

path = 'query-cosientist.md'
ev_tail = (" bench 2026-09-08 (第200回, K-Z3 9時台 n 積み増し run448A–C, 同測定法 n=20 \u00d7 3 + landing control, "
           "別接続 curl, Tokyo, 09:55:33–09:55:42 JST, 全 80/80 200, host load1 23.41 (09:55 uptime 実測, gate 7.5 大幅超過) "
           "は production HTTP 実測のため gate 外, secret 不含 \u2014 curl + python stats のみ): "
           "cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 run448A cold 散発ペア 2/20 (pos1 1.840s / pos4 0.877s 散発配置, "
           "warm 群 0.042\u20130.172s) p50 54.1ms max 1.840s / run448B cold 0/20 p50 46.6ms max 133.1ms / run448C cold 0/20 "
           "p50 48.3ms max 172.2ms, control (kotobase.net/signup) cold 0/20 p50 41.3ms max 143.9ms 完全静穏で control 分離成立、"
           "cold 群は search 側に局在。run448A 散発ペアは B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発/ペア型継続 "
           "(heavy>=6/20 は run331A 以降非再現継続)。9時台 (9/8) 通算 = run445 (2/60) + run446 (5/60) + run447 (2/60) + 本 tick run448 (2/60) "
           "= 11/240 (~4.6%) の 4 セット連続 cold>0 \u2014 朝帯 8時台 (8/420 ~1.9%) よりはやや高位の低\u301c中位帯候補で帯水準確定には rank 追加 n を要する。"
           "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")

lines = codecs.open(path, encoding='utf-8').read().split('\n')
# find K-Z3 row
idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 '):
        idx = i
        break
assert idx is not None, 'K-Z3 row not found'
lines[idx] = lines[idx].rstrip() + ev_tail

# insert iter-log entry right after '## Iteration log' header (line index)
hdr = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        hdr = i
        break
assert hdr is not None, 'Iteration log header not found'
ilog = ("- 2026-09-08: bench 第200回。09:55 JST tick。HEAD 9797280 = falsify 第198回 (09:50, K-Z3 9時台 n-add run447 cold 2/60, "
        "9時台 3 セット目) = remote net-kotobase/main 一致 (git fetch net-kotobase + rev-parse 比較 乖離 0; worktree detached HEAD のため "
        "fetch 系で取込, terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; "
        "search endpoint search.kotobase.net/search?q=test も 200 確認、本 tick 実測)。host load1 23.41 (09:55 uptime 実測, gate 7.5 大幅超過) "
        "のため local 測定は拒否 \u2014 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 "
        "n 積み増し継続」は stale (rank 第90回帯 artifact) \u2014 true progressive NEXT は iter-log HEAD 連鎖 (rank 第197回 \u2192 bench 第199回 "
        "run446 \u2192 falsify 第198回 run447) の「K-Z3 9時台 n 積み増し継続」で、本 tick は 9時台 4 セット目 run448A–C を実施 (run447 は falsify "
        "第198回 が使用済みのため次 run ID run448 使用)。run448 計測 (09:55:33–09:55:42 JST): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 "
        "run448A 散発ペア 2/20 (pos1 1.840s / pos4 0.877s) p50 54.1ms / B cold 0/20 p50 46.6ms / C cold 0/20 p50 48.3ms, "
        "control (kotobase.net/signup) 0/20 完全静穏 (max 143.9ms) で control 分離成立、cold 群 search 側局在、「帯内 1 窓即消失」散発単発/ペア型継続。"
        "9時台通算 run445+run446+run447+run448 = 11/240 (~4.6%) の 4 セット連続 cold>0 \u2014 朝帯 8時台 (8/420 ~1.9%) よりやや高位の低〜中位帯候補、"
        "帯水準確定には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。")

lines.insert(hdr + 1, ilog)
codecs.open(path, 'w', encoding='utf-8').write('\n'.join(lines))
print('OK append+ilog')
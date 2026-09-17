#!/usr/bin/env python3
# falsify 第115回: append K-Z3 evidence + iteration log entry
import io

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(docs, encoding='utf-8') as f:
    text = f.read()
lines = text.split('\n')

# locate K-Z3 row (starts with '| K-Z3 ')
kz3_idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 '):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'

EVID = (" falsify 2026-09-06 (第115回, K-Z3 22時台帯初計測 run252A-C, 同測定法 n=20 x 3 + landing control, "
"別接続 curl, Tokyo, 22:12:21-22:13:10 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 113.57 (22:12 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外 - "
"rank 第109回 NEXT「K-Z3 22時台帯初計測」に従い 現在時刻帯 22時台で実施): "
"cold(>=0.5s) 6/2/1 per 20 = 9/60 (~15.0%) - run252A heavy クラスタ 6/20 (1.0983/1.5631/1.6759/1.6829/1.8088/2.04s, "
"run 内散発配置 全 6 件, p50 171.6ms warm_p50 159.1ms) / run252B cold 2/20 (1.5509s/1.8335s) p50 143.3ms warm_p50 134.7ms / "
"run252C cold 1/20 (1.6914s) p50 142.3ms warm_p50 142.0ms, control (kotobase.net/signup) cold 1/20 (0.5707s 境界値) "
"p50 158.5ms - ※本 tick は host load 高騰 (113-194, gate 95 倍超) で search/control とも warm p50 全体的上振れ "
"(search warm 135-159ms, control 158ms vs 静穏帯 40-60ms) かつ control に 0.5707s の borderline cold 1 件が出現し "
"control 分離は borderline not-separated 傾向 (search 側 cold 9/60 自体は閾値決定的 - 全 9 件とも minimal 1.0983s で "
"0.5s 閾値を大きく超えるが control にも 1 件準同格が出たため機構判定としては弱い)。run252A heavy 6/20 クラスタは "
"従来「帯内1窓即消失」(1-4/60) を超える規模で B/C 0/20 の後 2 run では減衰し run232A 型 heavy burst の弱い類似 - "
"22時台帯初計測で 9/60 (~15.0%) は 21時台 (9/300 ~3.0%) や 9/5 22時台 (run172/173/174, 7/180 ~3.9%) と対比し明らかに高位で、"
"夜帯 traffic 遷移説とは逆の上振れ (host load 高騰 + control not-separated の混入で決定的反証には足りず、"
"低位帯ではなく高遅延帯としての 22時台サンプル 1 本)。status 判定は rank に委ねる (rank 専門).")

lines[kz3_idx] = lines[kz3_idx] + EVID

# iterate log: insert new entry after '## Iteration log'
ilog_idx = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        ilog_idx = i
        break
assert ilog_idx is not None, 'Iteration log header not found'

ILOG = ("- 2026-09-06: falsify 第115回。22:10 JST tick。worktree detached HEAD のため fetch net-kotobase + rev-parse "
"比較で取り込み (fetch rc 0, HEAD d545d0c = net-kotobase/main 先端一致, 乖離 0, bench/cosientist の並行 commit なし)。"
"rank 第109回 NEXT「K-Z3 22時台帯初計測」に従い 22時台で実施 (cron 時刻 22:10, 22時台のため待機不可 - "
"pre-run monitor の NEXT「深夜帯 23時台」は rank 第90回帯の stale と判断, 現在時刻帯 22時台を実施)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 144→113 (22:10/22:12 実測, gate 7.5 大幅超過) のため "
"local 測定は拒否し production HTTP フォールバック (gate 外)。K-Z3 run252A-C (同測定法 n=20 x 3 + landing control, "
"別接続 curl, 22:12:21-22:13:10 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): "
"cold(>=0.5s) 6/2/1 per 20 = 9/60 (~15.0%) - run252A heavy 6/20 クラスタ (6 件とも 1.098-2.04s) / run252B 2/20 / "
"run252C 1/20, control cold 1/20 (0.5707s 境界値)。22時台帯初計測 9/60 (~15.0%) は 21時台 (9/300 ~3.0%) と 9/5 22時台 "
"(7/180 ~3.9%) と対比し高位で夜帯 traffic 遷移説には逆方向の上振れ - ただし host load 高騰 (113-194) + control "
"not-separated (control cold 1 件) 混入で決定的反証には足りず clean-tick での再測定要 (帯水準確定は rank 判定に委ねる)。"
"status 遷移なし (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 22時台 n 積み増し継続, 次 run ID は run253 使用)。")

lines.insert(ilog_idx + 1, ILOG)

out = '\n'.join(lines)
with open(docs, 'w', encoding='utf-8') as f:
    f.write(out)
print('K-Z3 row len', len(EVID), 'inserted at line', kz3_idx + 1)
print('ILOG inserted after line', ilog_idx + 1)
print('done')
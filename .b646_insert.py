p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s = open(p, encoding='utf-8').read()

EV = ('cosientist 2026-09-16 (bench 23時台 tick, K-Z3 23時台 n 積み増し run646A-C, 同測定法 n=20 x3 + landing control, '
      '別接続 curl, Tokyo, 23:08-23:09 JST, 全 60/60 200 + control 20/20 200, 正 endpoint search.yataverse.com/search?q=test, '
      'host load1 19.83-26.35 (23:07-23:09 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python3 stats のみ): '
      'cold(>=0.5s) 6/2/0 per 20 = 8/60 (~13.3%) - run646A cold 6/20 (770.7-2297.8ms, 冒頭集中クラスタ) p50 156.4ms p95 1536.0ms / '
      'run646B cold 2/20 (808.6-1458.1ms 単発) p50 70.2ms / run646C cold 0/20 p50 66.6ms max 127.6ms 完全静穏, '
      'landing control (kotoba.cloud/, 同時刻 23:09, n=20, 全 200) cold 3/20 (506.1-612.9ms 単発群) p50 89.6ms max 612.9ms で本 tick は完全静穏ではなく部分的分離 '
      '(cold 率は同率級 15.0% vs 13.3%, ただし cold 下振れ幅は control 506-613ms に対し target 770-2298ms と深い - not-separated-leaning note)。'
      '23時台日差ペア: 9/7 23時台 ~11.3% 帯基準 vs 9/16 run646 8/60 (~13.3%), 同帯日次乖離 ×~1.2 で K-Z4 paired 材料継続。'
      'status 判定は rank に委ねる (rank 専門)。')

ITER = ('- 2026-09-16: bench (23:0x JST tick)。HEAD 73e96f0 = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため fetch net-kotobase + '
        'rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗のため不使用手順)。monitor: host load1 23.60 (23:08 pre-run 実測, gate 7.5 超過 '
        '— production HTTP 実測なら gate 外), live smoke 301/301 (kotobase.net/, /signup; 23:08 自検 0.045s/0.052s)。rank 第248回 NEXT「K-Z3 23時台 run646」に従い '
        '本 tick 時刻 (23時台) で K-Z3 23時台 n 積み増し run646A-C を実施 (同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 23:08-23:09 JST, 全 80/80 200): '
        'cold(>=0.5s) 6/2/0 per 20 = 8/60 (~13.3%) - A 6/20 冒頭集中 (770-2298ms) + B 2/20 単発 + C 0/20 完全静穏, control (kotoba.cloud/) 3/20 506-613ms 単発群で '
        '本 tick は control 完全静穏ならず部分的分離 (cold 率同率級 15.0% vs 13.3%, 下振れ幅は target 深め, not-separated-leaning note)。'
        '23時台は 9/7 ~11.3% に対し ~13.3% (同帯日差 ×~1.2, K-Z4 paired 継続)。evidence は本ファイル末尾に追記済み。status 判定は rank に委ねる (rank 専門)。'
        'NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 次 run ID は run647 使用)。secret 不含 (curl + python3 stats のみ)。\n')

# 1) evidence append at file end (rstrip, concat)
body = s.rstrip('\n')
body2 = body + '\n' + EV + '\n'

# 2) iter-log entry right after '## Iteration log' header line
marker = '## Iteration log'
i = body2.find(marker)
assert i >= 0
nl = body2.find('\n', i)
assert nl >= 0
body2 = body2[:nl+1] + ITER + body2[nl+1:]

open(p, 'w', encoding='utf-8').write(body2)
print('written, new bytes', len(body2))

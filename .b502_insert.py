P = 'query-cosientist.md'
with open(P, encoding='utf-8') as f:
    txt = f.read()
lines = txt.split('\n')

# --- verify L279 is K-Z3 row ---
idx = 278
line = lines[idx]
assert line.startswith('| K-Z3 |'), "L279 not K-Z3: %r" % line[:30]
assert line.rstrip().endswith('(rank 専門).') or 'status' in line, "L279 tail unexpected"

# run502 evidence measurement not already present (iter-log NEXT designation may reference run502; guard K-Z3 evidence row)
assert 'run502A' not in lines[idx], 'run502 evidence already in K-Z3 row'

# iter-log position
il_idx = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        il_idx = i
        break
assert il_idx is not None

ev = (' falsify 2026-09-08 (第223回, K-Z3 20時台 n 積み増し run502A-C - rank 第218回 NEXT "次 run ID は run502" の枠を実施 '
      '(iter-log HEAD rank 第218回), 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, '
      'nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:48:24-20:48:34 JST, '
      '全 80/80 200, host load1 29.31-43.00 (20:45 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, '
      'secret 不含 - curl + python stats のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) - '
      'run502A 単発 1/20 (1.0565s pos4) p50 57.2ms max 1056.5ms / run502B 単発 1/20 (1.0933s pos6) p50 59.0ms max 1093.3ms '
      '/ run502C cold 0/20 p50 50.6ms max 158.8ms, control (kotobase.net/signup) cold 0/20 p50 51.3ms max 154.9ms '
      '完全静穏で control 分離成立、cold 群は search 側に局在。run502A/B 各単発は C 0/20 + control 0/20 で即消失し '
      '「帯内 1 窓即消失」散発単発型継続 (run501A 散発クラスタ 4/20 (20:39) の ~9 分後、heavy>=6/20 は本 tick 非再現、'
      'heavy run487A 7/20 系も再現なし)。20時台 (9/8) 通算 = run499 (0/60, 帯初) + run500 (6/60) + run501 (4/60) + 本 tick run502 (2/60) '
      '= 12/240 (~5.0%) の 4 セット - 19時台 (9/240 ~3.8%) と同水準の晩側トランジション帯候補, '
      '日中高帯 (16-18時台 ~7.5-11.7%) より低位で traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。'
      '帯 n=4 セットで帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。')
ev = ev.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
assert '\u200b' not in ev and '\u200c' not in ev and '\u200d' not in ev
assert '\t' not in ev

lines[idx] = lines[idx].rstrip() + ev

il = ('- 2026-09-08: falsify 第223回。20:46 JST tick。HEAD 36d8ab7 = bench 第219回 (20:39, K-Z3 20時台 run501 cold 4/60). '
  'detached HEAD のため fetch 系で取込 (worktree 内に sibling rank 第218回 b5262ce が HEAD 上に commit 済みで remote main と一致, '
  '乖離 0)。terminal stdout 空=既知のため状態確認・計測出力はファイル書出経由。'
  'pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) - '
  'true progressive NEXT は rank 第218回 (Iteration log 最上部)「K-Z3 現在時刻帯 20時台 n 積み増し続行, 次 run ID は run502」の run502 枠を本 tick 実施。'
  'host load1 29.31-43.00 (20:45 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。'
  'live smoke 200 (/, /signup, search.kotobase.net/search?q=test; pre-run 計測)。'
  'K-Z3 20時台 n 積み増し run502A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, '
  'nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:48:24-20:48:34 JST, 全 80/80 200, '
  'secret 不含 - curl + python stats のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) - '
  'run502A 単発 1.0565s (pos4) p50 57.2ms / run502B 単発 1.0933s (pos6) p50 59.0ms / run502C 0/20 p50 50.6ms, '
  'control (kotobase.net/signup) 0/20 p50 51.3ms max 154.9ms 完全静穏で control 分離成立, cold 群 search 側局在。'
  'run502A/B 各単発は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 (run501A 4/20 の ~9 分後, '
  'heavy>=6/20 非再現)。20時台 (9/8) 通算 = run499 (0/60) + run500 (6/60) + run501 (4/60) + run502 (2/60) = 12/240 (~5.0%) 4 セット '
  '- 19時台 (9/240 ~3.8%) と同水準の晩側トランジション帯候補, traffic 依存説の日中帯方向支持継続, '
  '深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。'
  '詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切記録せず。'
  'NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run503 使用)')
il = il.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
assert '\u200b' not in il

lines.insert(il_idx + 1, il)

with open(P, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('INSERT_DONE new_lastline=%d' % (len(lines),))
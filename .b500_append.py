P = 'query-cosientist.md'
with open(P, encoding='utf-8') as f:
    txt = f.read()
lines = txt.split('\n')

# --- verify L279 is K-Z3 row ---
idx = 278
line = lines[idx]
assert line.startswith('| K-Z3 |'), "L279 not K-Z3: %r" % line[:30]
assert line.rstrip().endswith('(rank 専門).') or 'status' in line, "L279 tail unexpected: %r" % line[-60:]

# iter-log position
il_idx = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        il_idx = i
        break
assert il_idx is not None

ev = (' falsify 2026-09-08 (第222回, K-Z3 20時台・independent run500A-C, '
      '同測定法 n=20×3 + landing control, 別接続 curl, Tokyo, 20:27–20:29 JST, '
      '全 80/80 200, host load1 25.85–30 (production HTTP 実測のため gate 外)): '
      'SEARCH cold(>=0.5s) 6/60 (~10.0%) — run500A 散発クラスタ 6/20 '
      '(1.0529/1.2278/1.3050/1.3394/1.4019/1.6233s 冒頭ポジション) p50 171.6ms '
      '/ run500B 0/20 p50 139.1ms / run500C 0/20 p50 90.4ms — '
      'landing control (kotobase.net/signup, 同時刻, n=20, 全 200) cold 0/20 '
      'p50 194.5ms max 361.8ms 完全静穏で control 分離成立, cold 群は search 側に局在。'
      'run499 (bench 第218回, 20:11, 20時台帯初, cold 0/60 完全静穏) の約16分後 (20:28) に '
      '6/60 散発クラスタ (A 列のみ, B/C 0/40 即消失) — 20時台は帯初 0/60 → 帯内再上振れ 6/60 の '
      '「帯内 1 窓即消失」散発クラスタ型継続 (heavy run487A 7/20 級は再現なし), run499 の '
      '"完全静穏の一時低位窓" が日中高帯継続中の一時的低位である証左 (traffic 依存説の '
      '日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。'
      'status 判定は rank に委ねる (rank 専門).')
ev = ev.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
assert '\u200b' not in ev and '\u200c' not in ev and '\u200d' not in ev
assert '\t' not in ev

lines[idx] = lines[idx].rstrip() + ev

il = ('- 2026-09-08: falsify 第222回。20:29 JST tick。K-Z3 20時台 independent run500A–C 計測 '
  '(n=20×3 + landing control, 別接続 curl, search.kotobase.net/search?q=test, 20:27–20:29 JST, '
  '全 80/80 200, host load1 25.85–30): SEARCH cold(>=0.5s) 6/60 (~10.0%) — '
  'run500A 散発クラスタ 6/20 (1.05–1.62s), B/C 0/40 即消失, control (signup) 0/20 完全靜穏分離成立。'
  'run499 (bench 第218回, 20:11, 20時台帯初, 0/60 完全静穏) の ~16 分後の独立2セット目 — '
  '"帯内 1 窓即消失" 散発クラスタ型に一致 (run499 静穏は日中高帯中の一時低位窓), 20時台通算 6/120 (~5.0%)。'
  'status 判定は rank に委ねる (rank 専門). evidence は K-Z3 仮説行 (L279 末尾) に追記済み。')
il = il.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
assert '\u200b' not in il

lines.insert(il_idx + 1, il)

with open(P, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines) + '\n')
print('INSERT_DONE new_lastline=%d' % (len(lines),))
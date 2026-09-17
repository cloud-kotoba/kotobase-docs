import io
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines = open(p).read().splitlines(keepends=True)
anchor = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        anchor = i
        break
assert anchor is not None
evid = (' falsify 2026-09-05 (K-Z3 23時台 n 積み増し run175A–C, 同測定法 n=20 × 3 + landing control, '
        '別接続 curl, Tokyo, 22:59–23:00 JST, 全 80/80 200, host load1 10.5 は production HTTP 実測のため gate 外): '
        'run175A cold(>=0.5s) 0/20 p50 42ms max(除cold) 203ms / run175B cold 0/20 p50 40ms / run175C cold 0/20 p50 40ms '
        '— 合計 0/60, landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 47ms と静穏で control 分離成立。'
        '23時台第1計測は完全静穏 (深夜帯は run100 型の突発が残る可能性ありで継続観測)。status 判定は rank に委ねる (rank 専門)。')
if not lines[anchor].rstrip().endswith('|'):
    pass
lines[anchor] = lines[anchor].rstrip('\n').rstrip('|') + evid + ' |\n'
open(p, 'w').write(''.join(lines))
print('appended to K-Z3 line', anchor + 1)

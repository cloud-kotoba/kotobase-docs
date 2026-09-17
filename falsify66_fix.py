import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
txt = subprocess.run(['git','show','HEAD:query-cosientist.md'],cwd=d,capture_output=True,text=True).stdout
lines = txt.splitlines(keepends=True)
idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        idx = i
        break
assert idx is not None and lines[idx].rstrip().endswith('|')
evid = (' falsify 2026-09-05 (K-Z3 23時台 n 積み増し run175A–C, 同測定法 n=20 × 3 + landing control, '
        '別接続 curl, Tokyo, 22:59–23:00 JST, 全 80/80 200, host load1 10.5 は production HTTP 実測のため gate 外): '
        'run175A cold(>=0.5s) 0/20 p50 42ms max(除cold) 203ms / run175B cold 0/20 p50 40ms max 53ms / '
        'run175C cold 0/20 p50 40ms max 55ms — 合計 0/60 完全静穏, landing control (kotobase.net/, 同時刻, n=20, 全 200) '
        'は cold 0/20 p50 47ms と静穏で control 分離成立。23時台第1計測は完全静穏 (0時台 0/60 型と整合, 深夜帯突発の継続観測)。'
        'status 判定は rank に委ねる (rank 尚門)。')
lines[idx] = lines[idx].rstrip('\n').rstrip('|') + evid + ' |\n'
open(d + '/query-cosientist.md', 'w').write(''.join(lines))
print('ok, appended run175 evidence to K-Z3 line', idx + 1)

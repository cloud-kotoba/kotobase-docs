src = open('query-cosientist.md').read()
add = (' falsify 2026-09-05 (K-Z3 14時台 n 積み増し run153A–C, 同測定法 n=20 × 3 + '
       'landing control, 別接続 curl, Tokyo, 14:30–14:31 JST, 全 60/60 + control 20/20 200): '
       'run153A cold(>=1s) 0/20 p50 201.7ms max 416.3ms / run153B cold 0/20 p50 152.1ms '
       'max 279.6ms / run153C cold 0/20 p50 138.5ms max 322.6ms — landing control '
       '(kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 202.7ms と静穏。'
       '14時台初計測で 0/60 完全静穏 — status 判定は rank に委ねる。')
lines = src.split('\n')
for idx, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        pos = l.rfind('status 判定は rank に委ねる')
        assert pos != -1, 'marker not found in K-Z3 line'
        end = pos + len('status 判定は rank に委ねる')
        lines[idx] = l[:end] + add + l[end:]
        break
else:
    raise SystemExit('K-Z3 line not found')
open('query-cosientist.md', 'w').write('\n'.join(lines))
print('appended at line', idx + 1)

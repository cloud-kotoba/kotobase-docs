import io
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
idx = [i for i, l in enumerate(lines) if l.startswith('| K-Z3 |')]
assert len(idx) == 1, idx
i = idx[0]
ev = " falsify 2026-09-06 (K-Z3 8時台 1セット目 run195A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 08:01–08:02 JST, 全 80/80 200, host load1 214.45 は production HTTP 実測のため gate 外だが高負荷を注記): run195A cold(>=0.5s) 1/20 (0.641s 単発) p50 282ms / run195B cold 0/20 p50 185ms / run195C cold 0/20 p50 168ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) cold 0/20 p50 168ms で分離は borderline (search p50 全体的に control より上振れ気味, host load 急上昇 (~75→214) の混入可能性あり)。cold 1/60 単発で 8時台低位帯パターンと整合。status 判定は rank に委ねる (rank 専門)。"
# insert at end of the K-Z3 line, before its trailing newline
assert not lines[i+1].startswith(' '), 'next line is a continuation'
lines[i] = lines[i] + ev
open(p, 'w', encoding='utf-8').write('\n'.join(lines))
print('appended at line', i+1)

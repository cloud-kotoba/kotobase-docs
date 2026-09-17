#!/usr/bin/env python3
def parse(path):
    out = []
    with open(path) as f:
        for ln in f:
            t = ln.strip()
            if t:
                out.append(t)
    return out

stats = parse('.b189_run424_stats_out.txt')
a = stats[0]
b = stats[1]
c = stats[2]
ctl = stats[3]
lines = [
 'bench 2026-09-08 (bench 第189回, K-Z3 5時台 n 積み増し継続 run424A-C, 同測定法 n=20 x3 + landing control, 別接続 curl (separate conn, cold TTFB threshold guard), Tokyo, 05:55-05:57 JST, 全 80/80 200,) host load1 18.04 (gate 7.5 超過) は production HTTP 実測のため gate 外):',
 'run424A: ' + a,
 'run424B: ' + b,
 'run424C: ' + c,
 'landing control (kotobase.net/signup, 同時刻, n=20): ' + ctl,
 '=> 5時台通算 (run421 帯初 0/60 + 本 tick 0/60): cold 0/120 完全静穏 - run112/114 (通算 1/180) の静穏帯継続, cold 群なし, control 分離成立, status 判定は rank に委ねる.',
 ''
]
frag = '\n'.join(lines)
with open('.b189_run424_evidence.txt', 'w', encoding='utf-8') as f:
    f.write(frag)
print('evidence scratch len', len(frag))
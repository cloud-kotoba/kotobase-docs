import io
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()
anchor = 'status 判定は rank に委ねる (rank 専門)。\n\n## Iteration log'
assert s.count(anchor) == 1, 'anchor count=%d' % s.count(anchor)
ins = ('falsify 2026-09-06 (第100回, K-Z3 18時台 n 積み増し run230A–C, 同測定法 n=20 × 3 '
       '+ landing control, 別接続 curl, Tokyo, 18:03:14–18:03:59 JST, 全 80/80 200, '
       '正 endpoint search.kotobase.net/search?q=test, host load1 74.77 (18:00 uptime 実測, '
       'gate 7.5 大幅超過) は production HTTP 実測のため gate 外 — rank 第96回 NEXT「K-Z3 '
       '18時台 n 積み増し」に従い 18時台で実施): cold(>=0.5s) 0/1/0 per 20 = 1/60 (~1.7%) — '
       'run230A 0/20 p50 117.1ms max 380.0ms / run230B 単発 0.917s (2番目) p50 152.8ms / '
       'run230C 0/20 p50 191.1ms max 357.5ms, control (kotobase.net/signup) cold 1/20 '
       '(0.618s 境界値) p50 233.8ms max 617.8ms — ※本 tick は host load 高騰 (74.77) tick で '
       'search/control とも p50 全体的上振れ (search 117–191ms vs 静穏帯 40–60ms) かつ control '
       'に 0.618s の cold 1 件が出現し control 分離は borderline not-separated 傾向 (search 側 '
       'cold 1/60 自体は閾値決定的だが control にも cold 1 件が出たため機構判定としては弱い)。'
       'run230B 単発 1 件は A/C 0/20 で即消失し run222A/223A/225A/B/228A/B/C/229A 型'
       '「帯内 1 窓即消失」パターン継続 — 18時台帯初セットで cold 1/60 (~1.7%) の低位帯候補、'
       '17時台 (10/240 ~4.2%) と同水準の継続低温帯パターンを示すが control 分離の弱さから帯判定の'
       '確定には追加 n 要。status 判定は rank に委ねる (rank 専門)。'
       '\n')
new = s.replace(anchor, ins + anchor, 1)
io.open(p, 'w', encoding='utf-8', newline='\n').write(new)
print('anchor cnt=%d replaced' % s.count(anchor))
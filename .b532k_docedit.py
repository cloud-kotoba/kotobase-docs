import io, re
p = 'query-cosientist.md'
txt = io.open(p, encoding='utf-8').read()
n649 = txt.count('run649')
if n649 > 0:
    runid = 'run650 (bench; run649 ID collision 検出につき読替, run216/256/263 前例)'
else:
    runid = 'run649'
ev = (" 9/17 bench %s (2時台): 02:08-02:09 JST, search.yataverse.com/search?q=test 別接続 curl n=20x3 + control kotoba.cloud/ n=20, 全 60/60 200, cold(>=0.5s) 5/60 (~8.3%%) [A 2/20 (582.1/1009.3ms) + B 2/20 (636.8/981.4ms) + C 1/20 (776.8ms)], 各 p50 47.9-50.0ms, control 0/20 p50 66.2ms max 190.6ms 静穏で分離成立; 2時台 9/17 初 evidence (同夜隣接 1時台 run648 ~18.3%% より低く帯内日差材料, K-Z4 paired 継続)" % runid)
lines = txt.split('\n')
# append evidence to last K-Z3 row (no closing '|')
kz3 = [i for i, l in enumerate(lines) if l.startswith('| K-Z3 |')]
i = kz3[-1]
lines[i] = lines[i].rstrip() + ev
txt = '\n'.join(lines)
hdr = '## Iteration log'
hi = txt.index(hdr)
eol = txt.index('\n', hi) + 1
entry = "\n- 2026-09-17: bench (02:0x JST tick)。HEAD 0006b728 = fetch 後 net-kotobase/main 先端一致 (fetch net-kotobase + rev-parse 比較, git pull --ff-only 不使用手順)。monitor: host load1 21.77 (02:07 pre-run 実測, gate 7.5 超過 — production HTTP 実測のため gate 外), live smoke 301/301 (kotobase.net/, /signup)。pre-run monitor NEXT「23時台」は run646/647 で 9/16 消化済みにつき stale, cosientist 第160回 NEXT フォールバックに従い K-Z3 現在時刻帯 (2時台) n 積み増し %s を実施 (同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 02:08:00-02:08:29 JST, 全 60/60 200 + control 20/20 200): cold(>=0.5s) 5/60 (~8.3%%) - A 2/20 (582.1, 1009.3ms) + B 2/20 (636.8, 981.4ms) + C 1/20 (776.8ms), 各 p50 47.9-50.0ms, control (kotoba.cloud/) 0/20 p50 66.2ms max 190.6ms 完全静穏で分離成立。2時台 9/17 初 evidence, 同夜 1時台 run648 ~18.3%% との対比で 2時台は低め (K-Z4 同日帯ペア材料)。evidence は本ファイル K-Z3 行末尾に追記済み。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 次 run ID は run650 使用)。secret 不含 (curl + python3 stats のみ)。\n" % runid
txt = txt[:eol] + entry + txt[eol:]
io.open(p, 'w', encoding='utf-8').write(txt)
io.open('/tmp/b532k_docdone.txt', 'w').write("runid=%s kz3line=%d ok\n" % (runid, i))

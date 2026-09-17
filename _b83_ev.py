p = 'query-cosientist.md'
s = open(p).read()
lines = s.split('\n')
idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
        break
if idx is None:
    open('_b83_ev_out.txt', 'w').write('NO_KZ3_ROW\n')
else:
    line = lines[idx]
    ev = " bench 第83回 (13:13, 13時台帯初計測 run210A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 13:13:21–13:13:47 JST, 全 80/80 200, host load1 6.49 は production HTTP 実測のため gate 外): run210A cold(>=0.5s) 4/20 (0.829–1.057s 冒頭集中クラスタ) p50 48.2ms / run210B cold 1/20 (1.017s 単発) p50 35.9ms / run210C cold 1/20 (1.812s 単発) p50 41.8ms — cold 6/60 (~10%), landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 52.5ms max 64.3ms と静穏で control 分離成立、cold 群は search 側に局在。run210A 冒頭集中は run202A/207A/209A 型「帯内 1 窓即消失」パターン。13時台は帯初計測で 12時台 (7/120 ~5.8%) と同水準の低位帯寄り初期サンプル。status 判定は rank に委ねる (rank 専門)。"
    lines[idx] = line + ev
    open(p, 'w').write('\n'.join(lines))
    open('_b83_ev_out.txt', 'w').write(f'OK row {idx}\n')

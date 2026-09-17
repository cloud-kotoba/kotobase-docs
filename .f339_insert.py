# append falsify run339 evidence to K-Z3 row (L279) END only
LS=[l.rstrip('\n') for l in open('query-cosientist.md')]
row=LS[278]
assert row.startswith('| K-Z3 |'), 'row sanity'
INS=' falsify 2026-09-07 (第158回, K-Z3 11時台帯初計測 run339A\u2013C, 同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 11:05:39\u201311:06:09 JST, 全 80/80 200, host load1 70.44 (gate 7.5 超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 4/0/0 per 20 = 4/60 (~6.7%) \u2014 run339A 冒頭集中クラスタ 4/20 (1.123s/1.172s/1.262s/1.632s, 2\u20136番目 散発配置) p50 0.073s / run339B cold 0/20 p50 0.103s max 0.347s / run339C cold 0/20 p50 0.141s max 0.247s \u2014 landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 2/20 (0.517s/0.525s 閾値 0.5s ぎりぎりの境界値) p50 0.139s max 0.525s と概ね静穏だが境界値 2 件の borderline 注記付き \u2014 ただし cold 群は search 側に局在 (control の 0.5s 台 2 件 vs search 1.1\u20131.6s クラスタは逆方向で magnitude 分離成立)。run339A 冒頭集中は run202A/207A/209A/210A/211A 型「帯内 1 窓即消失」パターンと整合。11時台は帯初計測で 4/60 (~6.7%) の日中低位帯寄り初期サンプル。status 判定は rank に委ねる (rank 専門)。'
LS[278]=row+INS
open('query-cosientist.md','w').write('\n'.join(LS)+'\n')
print('appended, row len now', len(LS[278]))
# verify occurrence
c=open('query-cosientist.md').read().count('run339A')
print('run339A occurrence', c)
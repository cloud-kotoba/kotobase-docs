doc='query-cosientist.md'
s=open(doc,encoding='utf-8').read()
lines=s.split('\n')
# K-Z3 row = line 279 (index 278), starts with '| K-Z3 |'
ki=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |') and len(l)>1000:
        ki=i
        break
assert ki is not None, 'K-Z3 row not found'
assert lines[ki].rstrip('\n')==lines[ki], 'row ends without newline in string'
ev=' falsify 2026-09-13 第251回 (K-Z3 3時台 (9/13) n 積み増し, run593A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 03:26-03:28 JST, 全 80/80 200): cold(>=0.5s) search 10/1/0 per 20 = 11/60 (~18.3%) - run593A 散発クラスタ 9/20 (0.7796-1.8284s, max 1828.4ms) p50 81.0ms / run593B 単発 1/20 (1.5991s) p50 72.2ms / run593C 完全静穏 0/20 p50 67.0ms, control (kotobase.net/signup) cold 2/60 (0.6788/0.7115s 単発 2 窓) p50 72-84ms - control 非静穏で control 分離不成立 (run587/run590/run592 同型 not-separated 突発窓; search deep cold 0.78-1.83s 10 件は magnitude 逆方向で search 側濃厚局在傾向) - 深夜帯 23時台 run592 10/60 (~16.7%) に続き 3時台も中高位, 9/11 run577 (23時台, 02:08 注記) 型の深夜帯窓パターン継続で 23時台-3時台通しの深夜帯高位方向を支持; not-separated のため帯比率確定は clean-tick 追加 n 待ち。status 判定は rank に委ねる (rank 専門)。secret 不含 (curl + python3 stats のみ)。'
lines[ki]=lines[ki]+ev
open(doc,'w',encoding='utf-8').write('\n'.join(lines))
# verify occurrence
chk=open(doc,encoding='utf-8').read()
print('evcount=',chk.count('falsify 2026-09-13 第251回'))
print('KZ3rowlen=',len(lines[ki]))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Relabel my run521 measurement -> run522 (bench 第223回 consumed run521 at 01:23-24).
path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

kz3_idx = None
il_line = None
for i, ln in enumerate(lines):
    if kz3_idx is None and ln.startswith('| K-Z3 |'):
        kz3_idx = i
    if kz3_idx is not None and il_line is None and ln.startswith('- 2026-09-09: falsify 第232回'):
        if i > kz3_idx:
            il_line = i
if kz3_idx is None or il_line is None:
    raise SystemExit('ABORT anchor missing kz3_idx=%r il_line=%r' % (kz3_idx, il_line))
print('kz3_idx=', kz3_idx, 'il_line(0-based)=', il_line)

row = lines[kz3_idx]
before = row.count('run521')
row = row.replace('run521', 'run522')
row = row.replace(
    'の run522 枠として実施, 同測定法 n=20 x 3 + landing control, ',
    'の run522 枠として実施 (run521 は bench 第223回 01:23-24 が先行使用のため本測は run522 へ読替; read替 precedent run216/256/263/278), 同測定法 n=20 x 3 + landing control, ')
row = row.replace(
    '1時台 (9/9) 通算 = falsify run520 (4/60 ~6.7%) + 本 tick run522 (6/60) = 10/120 (~8.3%) 2 セット。',
    '1時台 (9/9) 通算 = falsify run520 (4/60) + bench run521 (3/60) + 本 tick run522 (6/60) = 13/180 (~7.2%) 3 セット - ただし bench run521 (01:23-24, control 完全静穏分離成立 3/60) と本 tick run522 (01:36-37, control 分離未成立) は独立サンプルで、本测 run522 は load spike 88 混入下の not-separated 寄り。')
lines[kz3_idx] = row
print('kz3 before run521 count=', before, '-> run522 x', row.count('run522'), 'run521 x', row.count('run521'))

IL = ("- 2026-09-09: falsify 第232回。01:37 JST tick。HEAD 7c24933 = rank 第229回 (NEXT run521; 新規 evidence 0)。"
"K-Z3 1時台 run522A-C 測定 (本測 run521 -> 読替 run522, bench 第223回 01:23-24 が run521 を先行使用): "
"TOTAL_SEARCH_COLD 6/60 (~10.0%) - run522A 3/20 (1.1363/1.3341/1.6646s) / run522B 2/20 (0.5134/0.5383s 境界) / "
"run522C 1/20 (0.8429s)、landing control 2/20 (0.5142/0.5933s) 完全静穏ならず control 分離未成立 (not-separated leaning)、"
"host load1 88 急上昇 tick で search p50 219-259ms の全体的上振れ混入濃厚。1時台 (9/9) 通算 = run520 4/60 + bench run521 3/60 + "
"本 tick run522 6/60 = 13/180 (~7.2%) 3 セット。K-Z3 仮説行 evidence 追記済み。\n")
lines[il_line] = IL
print('IL set.')

with open(path, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('written')

with open(path, 'r', encoding='utf-8') as f:
    allt = f.read()
print('wholefile run521=', allt.count('run521'))
print('wholefile run522=', allt.count('run522'))
rows = [ln for ln in lines if ln.startswith('| K-Z3 |')]
print('kz3 row run522=', rows[0].count('run522'), 'run521=', rows[0].count('run521'))
print('zwnbsp=', '\u200b' in allt)
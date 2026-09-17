#!/usr/bin/env python3
"""Append bench 140 (K-Z3 9時台 run331) evidence to K-Z3 row (line 279) in query-cosientist.md."""
path = 'query-cosientist.md'
with open(path, encoding='utf-8') as f:
    lines = f.read().split('\n')

txt = ''' bench 2026-09-07 (第140回, K-Z3 9時台 (現時刻帯) n-add run331A–C — HEAD falsify 第153回 (08:19) が run330 を消費済みで次 run ID run331, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 09:56–09:59 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 15.11 (09:52 開始時 21.67 → 09:56 測定時 15.11, gate 7.5 大幅超過だが production HTTP 実測のため gate 外), secret 不含 — curl のみ): cold(>=0.5s) 9/2/0 per 20 = 11/60 (~18.3%) — run331A cold 9/20 (idx1-5,7,9,10,19, 0.5–2.05s 帯 密集クラスタ) p50 68.9ms max 2047.7ms / run331B cold 2/20 (idx2,3) p50 50.2ms max 2046.6ms / run331C cold 0/20 p50 51.3ms max 64.7ms — landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 0/20 p50 52.9ms max 320.6ms と完全静穏で control 分離成立、cold 群は search 側に局在 (system-wide host load 由来でないことを control 静穏で支持)。*** 9時台帯初 run331A 9/20 は heavy run271A 6/20 型の再現 (>=6/20 クラスタ) で、run271A 以降 55 セット連続非再現を割る初の heavy 型再出現 — 「完全静穏/散発単発のみ」の近年読みへの重要な反証 (日中帯短時間スケール再発は消えておらず、1 窓に集中する heavy クラスタとして突発再現を示唆)。warm 側 p50 (50-69ms) は静穏基準 (~40-50ms) 並で、cold は search isolate 初回生成に局在。9時台 (9/7) 通算は本 tick run331 のみ (帯初 1 セット 11/60 ~18.3%)。heavy 型再出現のため K-Z3 */2 高頻度化要否の直接判断材料を更新、status 判定・機構判断は rank に委ねる (rank 専門).'''

# append to line 279 (index 278)
assert lines[278].rstrip().endswith('status 判定は rank に委ねる (rank 専門).'), "anchor mismatch"
lines[278] = lines[278].rstrip() + txt

with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('inserted; new line len', len(lines[278]))

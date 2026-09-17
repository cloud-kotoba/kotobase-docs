# Append bench 第162回 run371 evidence to the K-Z3 evidence row (L279).
# Direct plain-UTF-8 string append, same as falsify/bench precedent.
f='query-cosientist.md'
s=open(f,encoding='utf-8').read()
lines=s.split('\n')
idx=278  # line 279 (0-based)

entry = (' bench 2026-09-07 (第162回, K-Z3 16時台 4 セット目 run371A–C 積み増し, '
 '同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, '
 '正 endpoint search.kotobase.net/search?q=test, 16:26:35–16:27:06 JST, 全 80/80 200, '
 'host load1 29.3→36.2 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外): '
 'cold(>=0.5s) 5/3/0 per 20 = 8/60 (~13.3%) - '
 'run371A cold 5/20 (1.1343/1.2667/2.6386/1.0352/2.1582s 散発クラスタ, deep cold 2.64s) p50 143.9ms / '
 'run371B cold 3/20 (1.1029/1.1482/2.4062s 散発) p50 147.9ms / '
 'run371C cold 0/20 p50 143.5ms max 297.8ms - '
 'landing control (kotobase.net/signup, 同時刻, n=20, 全 200) は cold 1/20 (0.5328s 境界値) p50 148.8ms max 532.8ms で '
 '完全静穏不成立 borderline not-separated 注記 (control 境界 1 件のみ) だが search cold 8 件は 1.03–2.64s で '
 'control 境界 0.53s と逆方向の magnitude 分離弱成立、cold 群は search 側に局在。'
 'run371A 5/20 + run371B 3/20 の 2 run 跨散発クラスタは C 0/20 で帯内 1 窓即消失型継続 '
 '(run368A heavy 8/20 → run369 1/60 減衰 → run370 2/60 → run371A 5/20 + run371B 3/20 へ mid-clump 再上振れ, '
 'heavy>=6/20 は再達せず run331A 9/20 heavy 型の帯水準持続性は再現未確認)。'
 '16時台 (9/7) 通算 = run368 (9/60) + run369 (1/60) + run370 (2/60) + run371 (8/60) = 20/240 (~8.3%) 4 セット高位帯候補 '
 '(帯初 run368A heavy 8/20 の直後 run369 1/60 減衰 → run371 8/60 で再上振れ振幅大きな日中帯パターン, '
 'traffic 依存説の日中帯方向支持継続・深夜帯 ~26-31% 平坦パターンとの対比不変)。'
 'status 判定は rank に委ねる (rank 専門)。)')

lines[278] = lines[278] + entry
open(f,'w',encoding='utf-8').write('\n'.join(lines))
print('APPENDED. L279_LEN now', len(lines[278]))
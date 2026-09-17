#!/usr/bin/env python3
# -*- coding: utf-8 -*-
EVID = (" falsify 2026-09-09 (第232回, K-Z3 1時台 n 積み増し run521A-C - rank 第229回 NEXT "
"「K-Z3 現在時刻帯 1時台 n 積み増し (次 run ID は run521)」の run521 枠として実施, 同測定法 n=20 x 3 + landing control, "
"別接続 curl, Tokyo, 01:36-01:37 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, "
"host load1 88.73 (01:37 uptime 実測, gate 7.5 大幅超過 + 前tick 23->88 急上昇) は production HTTP 実測のため gate 外, "
"secret 不含 - curl のみ): cold(>=0.5s) 3/2/1 per 20 = 6/60 (~10.0%) - "
"run521A cold 3/20 (1.1363/1.3341/1.6646s) p50 219.3ms / run521B cold 2/20 (0.5134/0.5383s 閾値境界) p50 257.7ms / "
"run521C cold 1/20 (0.8429s) p50 254.0ms, control (kotobase.net/signup) cold 2/20 (0.5142/0.5933s) p50 259.4ms - "
"control が cold 2/20 出現し完全静穏でないため control 分離は未成立 (not-separated leaning), かつ search 全体の p50 (219-259ms) が "
"典型 ~43-55ms に対し大幅上振れで host load1 88 急上昇 tick の全体的上振れ混入が濃厚 (run521B の 0.51-0.54s 2 件は閾値ぎりぎり境界値, "
"cold 濃度 6/60 判定は load spike 混入下のため不確実)。1時台 (9/9) 通算 = falsify run520 (4/60 ~6.7%) + 本 tick run521 (6/60) = "
"10/120 (~8.3%) 2 セット。status 判定は rank に委ねる (rank 専門)。")

IL = ("- 2026-09-09: falsify 第232回。01:37 JST tick。HEAD 52912ca = rank 第228回 (1時台帯初 fold falsify231 run520 = 4/60 ~6.7%; "
"NEXT run521)。K-Z3 1時台 run521A-C 測定: TOTAL_SEARCH_COLD 6/60 (~10.0%) - run521A 3/20 (1.1363/1.3341/1.6646s) / "
"run521B 2/20 (0.5134/0.5383s 境界) / run521C 1/20 (0.8429s)、landing control 2/20 (0.5142/0.5933s) 完全静穏ならず "
"control 分離未成立 (not-separated leaning)、host load1 88 急上昇 tick で search p50 219-259ms の全体的上振れ混入濃厚。"
"K-Z3 仮説行 evidence 追記済み。")

for name, frag in (('EVID', EVID), ('IL', IL)):
    print(name, 'halt=', '\u200b' in frag, frag.count('\u200b'))
    import re
    print(name, 'hat4=', '#####' in frag, 'zwnbsp=', '\ufeff' in frag)
    # paren balance check
    print(name, 'paren_open=', frag.count('('), 'paren_close=', frag.count(')'))
    # strip to pure ASCII control scan
    ctrl = [hex(ord(c)) for c in frag if ord(c) < 32 and c not in '\n\t']
    print(name, 'ctrl=', ctrl)
#!/usr/bin/env python3
# Repair malformed edit from the bad insert script:
# - L280 (idx279) currently contains a DUPLICATE of bench-run406 evidence (was mistakenly set as ev)
#   -> replace with correct cosientist run407 evidence (with trailing newline)
# - L281 (idx280) currently is the leftover fragment "status 判定は rank に委ねる (rank 専門)。"
#   -> delete it
# L279 (idx278) keeps bench-184 run406 tail (correct).

PATH='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'

RUN407_EV = (
 '   cosientist 2026-09-07 (K-Z3 0時台(9/8) n 積み増し run407, 同測定法 n=20 × 3 + landing '
 'control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint '
 'search.kotobase.net/search?q=test, 00:07:36–00:07:47 JST, 全 80/80 200, host load1 7.77–8.54 '
 '(00:07 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 — '
 'curl + python stats のみ): cold(>=0.5s) 4/0/0 per 20 = 4/60 (~6.7%) — run407A cold 4/20 '
 '散発クラスタ (1.1520s/0.9739s/1.5461s/1.2697s) p50 54.4ms max 1.5461s / run407B cold 0/20 '
 'p50 51.3ms / run407C cold 0/20 p50 46.9ms, control (kotobase.net/signup) cold 0/20 '
 'p50 43.0ms max 172.4ms 完全静穏で control 分離成立、cold 群は search 側に局在。run407A '
 '散発クラスタ 4/20 は B/C 0/40 + control 0/20 即消失で「帯内 1 窓即消失」散発型継続 '
 '(heavy>=6/20 は再達せず)。0時台 (9/8 deep-night) 帯初計測 cold 4/60 (~6.7%) — 23時台 '
 '(9/7, ~11.3%) より低位の中位帯初期サンプル (帯初 n=1 セットで帯水準確定は rank 追加 n 待ち)。'
 'status 判定は rank に委ねる (rank 専門)。\n'
)

with open(PATH,'r',encoding='utf-8') as f:
    L=f.readlines()

# Validate indices: L279 (idx278) is the giant K-Z3 row; L280 (idx279) dup run406; L281 (idx280) fragment
prev = L[278]
dup = L[279]
frag = L[280]
print('L279 head:', prev[:30])
print('L279 len:', len(prev))
print('L280 starts bench-run406?:', dup[:40].startswith('   bench 2026-09-07 (第184回'))
print('L281 is status fragment?:', frag.strip() == 'status 判定は rank に委ねる (rank 専門)。')

assert prev.startswith('| K-Z3 | worker |'), 'L279 is not K-Z3 row'
assert dup[:20].count('bench')>0 and 'run406' in dup, 'L280 is not dup run406'
assert frag.strip().startswith('status 判定は rank に委ねる'), 'L281 not fragment'

# Repair: replace L280 with run407 evidence, drop L281
L[279] = RUN407_EV
del L[280]

with open(PATH,'w',encoding='utf-8') as f:
    f.write(''.join(L))
print('REPAIRED OK')
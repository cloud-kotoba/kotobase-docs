p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(p) as f:
    lines=f.read().split('\n')

idx=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        idx=i; break
assert idx is not None

anchor = 'secret は一切記録せず。'
ev = (' bench 2026-09-07 (第137回, K-Z3 7時台 n 積み増し run325A–C — run324 は falsify 第150回 (07:34) '
      'が先行使用済みの 7時台帯 n 積み増し, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, '
      '07:40–07:41 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 171 '
      '(07:39 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): '
      'cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run325A 単発 1.5941s (16番目 散発) p50 0.169s max 1.594s '
      '/ run325B cold 0/20 p50 0.138s max 0.334s / run325C cold 0/20 p50 0.188s max 0.281s, '
      'control (kotobase.net/signup) cold 0/20 p50 0.143s max 0.277s 完全静穏で control 分離成立、'
      'cold 群は search 側に局在。run325A 単発は B/C 0/20 + control 0/20 で即消失し'
      '「帯内 1 窓即消失」散発単発型継続 (run324A 6/20 heavy 汚染 borderline 後の散発減弱, heavy run271A 型は '
      'run271A 以降 51 セット連続非再現)。7時台通算算入は rank 判定に委ねる (run321 3/60 + run322-indep 2/60 '
      '+ run323 1/60 + 本 run325 1/60, run324 6/60 not-separated 算入可否含む)。status 判定は rank に委ねる '
      '(rank 専門)。secret は一切記録せず。')

nl = lines[idx] + ev
lines[idx]=nl
with open(p,'w') as f:
    f.write('\n'.join(lines))

# verify tail
print('VERIFY TAIL:', repr(lines[idx][-500:]))
print('new len', len(lines[idx]))
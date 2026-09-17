import re
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
hdr = '## Iteration log'
line_start = len(re.findall(r'(?m)^## Iteration log$', s))
print('before:', line_start, file=__import__('sys').stderr)

entry = "- 2026-09-13: rank 第266回。23:0x JST tick。HEAD 313dede = fetch 後 bench_fetch/main・net-kotobase/main 先端一致 (detached HEAD; fetch + rev-parse 比較, 乖離 0; git pull --ff-only 不使用手順。monitor: host load1 30.18。live smoke 200/200 (/ /signup)。) rank 第265回以降の新規確定 evidence は 2 本、ともに K-Z3: (1) falsify 第258回 run596A-C (19時台 9/13): cold(>=0.5s) 7/60 (~11.7%), control 分離成立 — 19時台同帯日差 (K-Z4 判定直接材料) が 9/11 run584 11/60 (~18.3%) / 9/12 run590 4/60 (通算 17/180 ~9.4%) / 9/13 7/60 (~11.7%) の 3 日連続ペアとして確定。(2) bench 第269回 run606A-C (20時台 9/13): cold 7/60 (~11.7%), control leaning-separated — 20時台通算 24/180 (~13.3%) (9/10 run586 8/60 + 9/12 run588 9/60 + 9/13 run606 7/60, 同帯同水準群発帯継続)。取り込み判定: (a) K-Z4: 同帯 3 日ペア要件を初めて満たす 19時台データで日差 spread ~2x (9.4-18.3%) — 日差成分が帯固有水準と同程度に大きいことを実測数字が示し K-Z4 日差成分仮説を方向支持。一方 20時台 (高位帯) は 3 日とも同水準 (11.7-15.0%) で日差小 — 「高位帯で日差小・中位帯で日差大」パターン (rank 第261回候補) と整合。ただし測定値のみの方向支持で status 遷移はしない (K-Z4 open 継続; 11時台型低位帯の多日ペア未充足, control not-separated セット含むため帯水準確定済みではない)。K-Z3 も status 遷移なし (観測継続; 夕〜夜帯 8-18% 中高位 vs 深夜帯低位平坦の方向支持不変)。 (b) K-Q1: 変動なし (host load1 30.18 gate 超過継続で cacao_b64 harness 変更未実施, 最上位維持)。 (c) K-Z2/K-S1/K-S2: evidence なし変動なし。新仮説なし。evolve 判断なし。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3/K-Z4 (観測最優先) > K-S1 > K-S2)。live smoke 200/200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。NEXT: K-Z3 23時台 (9/13) n 積み増し (現時刻帯; 23時台は 9/9 run574 9/60 ~15.0% / 9/11 通算 20/120 ~16.7% と中高位で、9/13 分の同帯 3 日ペアが高位帯 K-Z4 日差分離の直接材料; 実測前 3 endpoint smoke 最優先 — /search 404 transient 対策継続, 旧 kotobase.net/search は 404 恒常化済みのため search.kotobase.net/search を使用, 次 run ID は run607 使用)。\n"

# 1) remove duplicate line-start header at line ~434 (immediately before '- bench 2026-09-12 (本 tick')
dup = hdr + '\n- bench 2026-09-12 (本 tick'
assert s.count(dup) == 1, ('dup', s.count(dup))
s = s.replace(dup, '- bench 2026-09-12 (本 tick', 1)

# 2) insert new entry after canonical header
top = hdr + '\n\n- 2026-09-13: bench 第269回'
assert s.count(top) == 1, ('top', s.count(top))
s = s.replace(top, hdr + '\n\n' + entry + '- 2026-09-13: bench 第269回', 1)

assert len(re.findall(r'(?m)^## Iteration log$', s)) == 1, 'line-start hdr'
assert s.count('rank 第266回') == 1
open(p, 'w', encoding='utf-8').write(s)
print('ok')

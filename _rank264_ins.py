import io,re
p='query-cosientist.md'
s=io.open(p,encoding='utf-8').read()
hdrs=[m.start() for m in re.finditer(r'^## Iteration log',s,re.M)]
assert len(hdrs)==2, len(hdrs)
s=re.sub(r'^## Iteration log\n- bench 2026-09-12 \(本 tick, K-Z3 23時台 n 積み増し run592A-C',lambda m:'\n- bench 2026-09-12 (本 tick, K-Z3 23時台 n 積み増し run592A-C',s,count=1,flags=re.M)
hdrs=[m.start() for m in re.finditer(r'^## Iteration log',s,re.M)]
assert len(hdrs)==1, len(hdrs)
assert 'rank 第264回' not in s
anchor='- 2026-09-12: rank 第263回。'
i=s.find(anchor)
assert i>=0
entry="- 2026-09-13: rank 第264回。03:0x JST tick。HEAD 6998d2d = bench 第553回 (run592A-C, 23:09 9/12, K-Z3 23時台 n 積み増し cold 10/60 ~16.7%, control 5/20 非静穏 not-separated 突発窓型 — 帯比率採用保留のまま clean-tick 追加 n 待ち) = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 手順; git pull --ff-only は silent 失敗のため不使用; terminal foreground stdout 空=既知のため状態確認はファイル書出経由)。rank 第263回 (fd293e6, 19:04 9/12) 以降の新規確定 evidence は 3 本、すべて K-Z3 9/12: (1) falsify 第250回 run590A-C (19:38, commit 8df5810): 19時台 n 積み増し cold 4/60 (~6.7%), control 1/20 (1.1524s deep cold 単発) not-separated — 19時台 (9/12) 通算 17/180 (~9.4%), 9/11 run584 11/60 (~18.3%) 対比は低め側で同帯日差 (K-Z4 材料)。(2) bench 第552回 run588A-C (20:08, commit b8be7b3): 20時台 (9/12) 帯初 cold 9/60 (~15.0%) — run588A heavy 散発クラスタ 8/20, control 1/20 境界値 borderline not-separated-leaning。20時台同帯日差: 9/10 run586 8/60 (~13.3%) vs 9/12 run588 9/60 (~15.0%) 同水準中高位。(3) bench 第553回 run592A-C (23:09, commit 6998d2d): 23時台 (9/12) n 積み増し cold 10/60 (~16.7%) — run592A 散発クラスタ 8/20 (max 4.3222s), control 5/20 (0.530–1.159s) 非静穏で not-separated (clean-tick 追加 n まで帯比率採用保留)。取り込み判定: (a) K-Z3: run590+run588+run592 を fold。夕〜夜帯 (19/20/23時台) が 9/12 も 6.7–16.7% 中高位継続 (9/10–9/11 の 13.3–18.3% と同水準) — 深夜帯低位平坦 (2–9%) との対比は不変で traffic 依存説の方向支持継続。ただし本日 3 run とも control not-separated/borderline (run583/run584/run587/run588 系突発窓が endpoint 横断的に頻発) で機構判別 (query 側 vs edge/traffic 側) は引き続き阻害され、決定的支持/反証に未達 → status 遷移なし (K-Z3 open 継続)。23時台同帯日差: 9/9 run574 9/60 (~15.0%) vs 9/11 20/120 (~16.7%) vs 9/12 run592 10/60 (not-separated 保留込みで概ね同水準) — 高位帯は日差小の K-Z4 候補パターンを弱く継続。(b) K-Z4: 11時台 (1.7/16.7/8.3%) と 19/20/23時台 (日差小・中高位安定) の帯依存日差候補は材料継続だが、分離判定に足る同帯連続日ペア (n>=2 sets/day × 2 日以上, clean-tick) は未充足で evidence なしのまま open。(c) K-Q1: 変動なし — host load1 9.31 (pre-run monitor, gate 7.5 超過継続) で cacao_b64 harness 変更未実施, 最上位維持。(d) K-Z2/K-S1/K-S2: evidence なし変動なし。新仮説なし。evolve 判断なし。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200/200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。NEXT: K-Z3 3時台 (9/13, 現時刻帯深夜最低帯) n 積み増し — 9/12 突発窓 (control not-separated 3 run 連続) の clean-tick 対比として深夜最低帯静穏パターン (過去 2時台 ~1.9-2.5%) の再確認が機構判別 (突発窓が帯横断か traffic 依存か) の直接材料。\n\n"
s=s[:i]+entry+s[i:]
io.open(p,'w',encoding='utf-8').write(s)
print('OK')

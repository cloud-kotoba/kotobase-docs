import io, sys

p = "query-cosientist.md"
doc = io.open(p, encoding="utf-8").read()

# 1) Insert rank 260 entry at top of Iteration log (consume header, re-emit once)
hdr = "## Iteration log\n"
i = doc.find("\n" + hdr)
assert i >= 0, "iter header not found"
assert doc.count(hdr) == 1, "duplicate iter header"

entry = ("## Iteration log\n"
"- 2026-09-11: rank 第260回。23:0x JST tick。HEAD 029b265 = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 手順; git pull --ff-only は silent 失敗のため不使用; pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale artifact — true progressive NEXT は iter-log HEAD 連鎖)。rank 第259回 (3ce1c7b) 以降の新規確定 evidence は 3 本すべて K-Z3: (1) bench 第219回 run583A-C (17時台 9/11, 8ad1e1f): cold 11/60 (~18.3%) — run583A 散発クラスタ 9/20, control 7/20 非静穏で分離不成立 (not-separated 突発窓)。(2) falsify 第248回 run584A-C (19時台, 3ede3dd): cold 11/60 (~18.3%) — run584A heavy 9/20 (0.975-2.203s), control 1/20 borderline-leaning, 19時台通算 21/180 (~11.7%)。(3) bench 第434回 run586A-C (20時台 9/10, worktree in-flight 取り込み): cold 8/60 (~13.3%) — control 0/20 完全静穏で分離成立, 9/7 20時台 (run392-396 群発) と同型散発群発帯。取り込み判定: (a) K-Z3 open 観測継続 — 夕〜夜帯 (17/19/20時台) が複数日 8-18% 中高位で「1 窓クラスタ + 即消失」散発型の再現継続 (深夜帯 2-9% 低位・平坦との対比) は時間帯依存 (traffic 依存説) を方向支持。ただし control not-separated 突発窓 (run583/run584/run578/run582 系) が夕〜夜帯に頻発し endpoint 横断的である点は機構 (query 側 vs edge/traffic 側) 判別を阻害 — 決定的支持/反証に未達で status 遷移なし。同一帯日差 (11時台 9/9 ~1.7% vs 9/10 ~16.7% vs 9/11 ~8.3%) は K-Z4 として本 tick 表行登録 (open, evidence なし)。 (b) K-Q1: 変動なし (host load1 43.48 pre-run, gate 7.5 超過継続で harness 変更未実施, 最上位維持)。 (c) K-Z2/K-S1/K-S2: evidence なし変動なし。evolve 判断なし。live smoke 200/200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。NEXT: K-Z3 23時台 n 積み増し (現時刻帯, 9/9 run574 帯初 9/60 (~15.0%) との同帯日差対比が K-Z4 判定の直接材料)。\n")
doc = doc[:i+1] + entry + doc[i+1:]

# 2) Register K-Z4 table row after the 2nd K-Z3 row
lines = doc.split("\n")
idxs = [k for k, l in enumerate(lines) if l.startswith("| K-Z3 |")]
assert len(idxs) == 2, "K-Z3 rows != 2"
kz4 = "| K-Z4 | worker | K-Z3 系の同一時間帯における cold 発現率の日次変動 (11時台 9/9 4/240 ~1.7% vs 9/10 run572 10/60 ~16.7% vs 9/11 run578+579 10/120 ~8.3% 等) は帯固有水準ではなく日次 traffic 変動成分を含む — 同一帯の連続日ペア測定 (n>=2 sets/day × 2 日以上) で日差成分を帯平均から分離し、*/2 高頻度化・時間帯別発火の要否判断の帯間比較を補正する | open | — |"
lines.insert(idxs[1] + 1, kz4)
doc = "\n".join(lines)

io.open(p, "w", encoding="utf-8").write(doc)
print("OK")

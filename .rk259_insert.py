import io, sys

path = "query-cosientist.md"
doc = io.open(path, encoding="utf-8").read()

hdr = doc.count("## Iteration log")
checks = []
checks.append(("hdr==1", hdr == 1))
checks.append(("no run579", "run579A" not in doc))
checks.append(("no rank259", "rank 第259回" not in doc))
checks.append(("no K-Z4 row", "| K-Z4 |" not in doc))
anchor_ks1 = "| K-S1 | storage |"
checks.append(("ks1 present", anchor_ks1 in doc))
anchor_r258 = "## Iteration log\n\n- 2026-09-11: rank 第258回"
checks.append(("r258 anchor", anchor_r258 in doc))
if not all(ok for _, ok in checks):
    print("PRECHECK_FAIL", checks)
    sys.exit(1)

kz4_row = ("| K-Z4 | worker | K-Z3 の帯別発現率差のうち「帯差 (時間帯固定成分)」と「日次変動差」を分離する — 同一時間帯の連続日ペア測定 "
           "(n>=2 sets/day × 複数日) で日差成分を帯平均から分離し、*/2 高頻度化の要否判断に必要な時間帯×日次分解を確定する "
           "| 初期サンプル: 1時台 (9/10) run575A-C cold 11/60 (~18.3%) と 1時台 (9/11) run579A-C cold 11/60 (~18.3%) — 同帯 2 日連続同値 "
           "(帯固定成分候補) だが各日 n=1 セットのため日差成分分離には同一帯の複数セット/日を要する "
           "(run579 は sibling 孤児測定の生 snapshot .b579_stats_snapshot.txt 照合済み採用) | open | — |\n")
doc = doc.replace(anchor_ks1, kz4_row + anchor_ks1, 1)

entry = ("- 2026-09-11: rank 第259回。07:03 JST tick。HEAD 125b777 = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 "
         "(fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; git pull --ff-only は silent 失敗のため fetch 手順; "
         "terminal foreground stdout 空=既知のため状態確認はファイル書出経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続」は "
         "stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第258回 NEXT「K-Z3 3時台 (9/11) run578」))。"
         "rank 第258回以降の新規確定 evidence は 1 本: sibling 孤児 run579A-C (9/11 01:34 JST, 1時台 n 積み増し — 実測後 commit 断絶の worktree 孤児, "
         ".b579_stats_snapshot.txt 生データ照合済み採用, rank 第257回 run572 孤児前例; rank 第258回 NEXT「K-Z3 3時台 run578」は 3時台枠として未消費のまま "
         "3時台 (9/11) 帯欠測注記): cold(>=0.5s) 8/1/2 per 20 = 11/60 (~18.3%) — run579A heavy 8/20 (0.9161–1.6291s) p50 59.8ms p95 1606.7ms / "
         "run579B 単発 1/20 (0.8863s) p50 42.2ms / run579C 散発 2/20 (0.9177/1.6505s) p50 44.0ms, control (kotobase.net/signup) cold 0/20 p50 49.5ms "
         "max 265.6ms 完全静穏で control 分離成立, host load1 5.25 (01:34 1min 実測, gate 7.5 未満の quiet tick) は production HTTP 実測のため gate 外。"
         "取り込み判定: (a) K-Z3: run579 を 1時台 (9/11) 積み増しとして fold — 1時台 (9/10) run575 11/60 (~18.3%) と 2 日連続同値で 1時台高位帯の帯固定成分候補を強める, "
         "run579A heavy 8/20 は run575A 11/20 に続く heavy>=6/20 クラスタ連続再現継続 (run573A 9/20 → run574A 7/20 → run575A 11/20 → run579A 8/20)。"
         "K-Z3 status 遷移なし (open 観測継続, 決定的支持/反証に未達)。(b) 新仮説登録: K-Z4 (worker) を表行込みで登録 (rank 第258回「帯差 vs 日差の分離」候補の確定) — "
         "初期 evidence に 1時台 2 日ペア (run575/run579 同値 11/60) を採用, rank 順位は K-Q1 > K-Z2 > K-Z3 > K-Z4 > K-S1 > K-S2 (初期 n 不足のため K-Z3 直下)。"
         "(c) K-Q1: 変動なし — host load1 20.34 (07:02 pre-run monitor, gate 7.5 大幅超過) で cacao_b64 harness 変更は未実施のまま低負荷 tick 待ち, 最上位維持。"
         "(d) K-Z2/K-S1/K-S2: evidence なし (変動なし)。evolve 判断なし (確認済み勝ち仮説なし)。live smoke 200/200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。"
         "NEXT: K-Z3 7時台 (9/11) 帯初計測 (帯未計測なら帯初計測; 9/8 7時台 ~1.7-2.2% 低位帯の 3 日目対比で帯固定 vs 日差を切る K-Z4 初期データも兼ねる; "
         "次 run ID は run580 使用 — worktree に sibling bench の .b580 runner 準備痕があり先行消費時は run581 に読替, 定例 precedent)。")
doc = doc.replace(anchor_r258, "## Iteration log\n\n" + entry + "\n\n- 2026-09-11: rank 第258回", 1)

io.open(path, "w", encoding="utf-8").write(doc)

doc2 = io.open(path, encoding="utf-8").read()
post = [
    ("hdr==1", doc2.count("## Iteration log") == 1),
    ("rank259 present", "rank 第259回。07:03 JST tick" in doc2),
    ("rank258 preserved", anchor_r258 in doc2),
    ("K-Z4 row present", "| K-Z4 | worker |" in doc2),
    ("run579 present", "run579A" in doc2),
]
print("POSTCHECK", post, "ALL_OK" if all(ok for _, ok in post) else "FAIL")

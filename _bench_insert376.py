import io, sys
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
text = io.open(p, "r", encoding="utf-8").read()
lines = text.split("\n")

ITER_ENTRY = (
"- 2026-09-07: bench 第165回。17:16 JST tick。HEAD c749d7e = remote net-kotobase/main 一致 "
"(fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, "
"fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。"
"live smoke 200 (/, /signup; pre-run + 本 tick 実測)。host load1 100.94 (17:07 uptime 実測, "
"gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact — "
"全 bot 共有判断済み) — true progressive NEXT は iter-log HEAD (cosientist 第125回, 17:03) "
"「委ねる; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し続行、次 run ID は run376 使用」の "
"run376 枠を本 tick 実施 (17時台 2 セット目, cosientist 第125回 run375 17時台帯初 4/60 済みの "
"積み増し続行; run376 は NEXT 指定の次 ID で衝突なし確認)。K-Z3 17時台 run376A–C 実測 "
"(同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
"正 endpoint search.kotobase.net/search?q=test, 17:14–17:16 JST, 全 80/80 200, "
"secret 不含 — curl のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%) — run376A cold 5/20 "
"散発クラスタ (0.9865/1.2754/1.9451/0.9722/0.9888s 散発配置) p50 57.2ms warm_p50 56.2ms / "
"run376B cold 1/20 (1.0034s 単発) p50 57.9ms / run376C cold 0/20 p50 55.1ms max 105ms, "
"control (kotobase.net/signup) cold 0/20 p50 54.3ms max 300.3ms 完全静穏で control 分離成立、"
"cold 群は search 側に局在。run376A 散発クラスタ 5/20 は B 単発 1/60 + C 0/20 + control 0/20 で "
"「帯内 1 窓即消失」型継続 (heavy>=6/20 は再達せず run368A/373A heavy 型は非再現継続, "
"host load1 100 高騰 tick だが control 0/20 完全静穏で cold 濃度 6/60 は閾値決定的)。17時台 (9/7) "
"通算 = run375 (4/60) + 本 tick run376 (6/60) = 10/120 (~8.3%) の 2 セット中位帯候補 — 16時台 (9/7) "
"33/360 ~9.2% 高位帯候補に続く日中帯高位方向の帯横断追加観測 (traffic 依存説の日中帯方向支持継続, "
"深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"
"secret は一切記録せず (curl のみ + 統計 python ファイル)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し続行、"
"次 run ID は run377 使用)"
)

KZ_FRAGMENT = (
" bench 2026-09-07 (第165回, K-Z3 17時台 n 積み増し run376A–C — cosientist 第125回 run375 "
"(17時台帯初, 17:03) に続く 17時台 2 セット目, 同測定法 n=20 × 3 + landing control, "
"別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
"17:14–17:16 JST, 全 80/80 200, host load1 100.94 は production HTTP 実測のため gate 外, "
"secret 不含 — curl のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%) — run376A cold 5/20 "
"散発クラスタ (0.9865s/1.2754s/1.9451s/0.9722s/0.9888s) p50 57.2ms / run376B cold 1/20 "
"(1.0034s 単発) p50 57.9ms / run376C cold 0/20 p50 55.1ms, control (kotobase.net/signup) "
"cold 0/20 p50 54.3ms max 300.3ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run376A 散発 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」型継続 "
"(heavy>=6/20 は再達せず)。17時台 (9/7) 通算 10/120 (~8.3%) 2 セット中位帯候補。"
"status 判定は rank に委ねる (rank 専門)。"
)

# 1) iter-log insert (newest-first): after "## Iteration log" header line
il_idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        il_idx = i
        break
if il_idx is None:
    sys.stderr.write("Iteration log marker not found\n"); sys.exit(1)
lines.insert(il_idx + 1, ITER_ENTRY)

# 2) K-Z3 evidence cell append: at end of the physical line starting "| K-Z3 | worker |"
kz_idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        kz_idx = i
        break
if kz_idx is None:
    sys.stderr.write("K-Z3 row not found\n"); sys.exit(1)
lines[kz_idx] = lines[kz_idx] + KZ_FRAGMENT

io.open(p, "w", encoding="utf-8", newline="\n").write("\n".join(lines))
sys.stderr.write("OK inserted kz_idx=%d il_idx=%d\n" % (kz_idx, il_idx))
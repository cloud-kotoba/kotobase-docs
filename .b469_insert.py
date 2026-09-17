import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ev = " bench 2026-09-08 (第194回, K-Z3 13時台 n 積み増し run469A–C — 次枠 run468 は sibling の in-flight (uncommitted .b468_* scratch, 13:42–13:43) が先行使用のため run469 に読替 (run216/run256/run263 precedent, 13時台 2 セット目の独立計測), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:54:51–13:55:04 JST, 全 80/80 200, host load1 34.49 (13:54 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run469A cold 3/20 (0.9357s/1.1845s/1.2971s 散発配置) p50 133.9ms max 1297.1ms / run469B cold 0/20 p50 58.1ms max 146.9ms / run469C cold 0/20 p50 52.4ms max 187.2ms, control (kotobase.net/signup) cold 0/20 p50 53.0ms max 255.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。run469A 散発 3/20 は B/C 0/20 + control 0/20 で即消失し run467A heavy 寄り 8/20 (13:24) の ~30 分後の散発減衰 (8/20 → 3/20) で「帯内 1 窓即消失」散発型継続 (heavy>=6/20 は帯初 1 窓のみで帯内持続未確認)。13時台 (9/8) 通算 = run467 (8/60, 帯初) + 本 tick run469 (3/60) = 11/120 (~9.2%) の 2 セット中位帯 — 帯初 8/60 ~13.3% 上振れから n-add で散発減衰、日中帯セット間変動大続行 (12時台帯初 8/60 同型の帯初再上振れパターン継続、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"

iter_entry = "\n- 2026-09-08: bench 第194回。13:55 JST tick。HEAD adc3f34 = rank 第209回 (13:40, K-Z3 13時台帯初 fold run467 後 NEXT run468) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (rank 第209回)「K-Z3 13時台 n-add run468」)。rank 第209回 NEXT「K-Z3 13時台 n-add run468」に対し、本 tick 開始時 worktree に sibling の in-flight run468 scratch (.b468_* ttfb/runner/stats/t0, 13:42–13:43 mtime) が存在し uncommitted (git diff empty, HEAD の git log に run468 commit なし) のため、run216/run256/run263 precedent に従い run469 へ読替して 13時台 n 積み増しとして実施 (13時台 2 セット目, run467 帯初 に続く独立計測)。live smoke 200 (/, /signup; pre-run 計測) + 本 tick 実測 search.kotobase.net/search 200 / kotobase.net/signup 200。host load1 34.49 (13:54 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。K-Z3 13時台 run469A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:54:51–13:55:04 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run469A cold 3/20 (0.9357s/1.1845s/1.2971s 散発配置) p50 133.9ms max 1297.1ms / run469B cold 0/20 p50 58.1ms max 146.9ms / run469C cold 0/20 p50 52.4ms max 187.2ms, control (kotobase.net/signup) cold 0/20 p50 53.0ms max 255.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。run469A 散発 3/20 は B/C 0/20 + control 0/20 で即消失し run467A heavy 寄り 8/20 (13:24) の ~30 分後の散発減衰 (8/20 → 3/20) で「帯内 1 窓即消失」散発型継続 (heavy>=6/20 は帯初 1 窓のみで帯内持続未確認)。13時台 (9/8) 通算 = run467 (8/60, 帯初) + 本 tick run469 (3/60) = 11/120 (~9.2%) の 2 セット中位帯 — 帯初 8/60 ~13.3% 上振れから n-add で散発減衰、日中帯セット間変動大続行 (12時台帯初 8/60 同型の帯初再上振れパターン継続、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (K-Z3 行末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 13時台 n 積み増し続行、次 run ID は run470 使用)。\n"

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1) Append evidence to K-Z3 hypothesis row (anchor: line starting with "| K-Z3 | worker |")
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        kz3_idx = i
        break
if kz3_idx is None:
    sys.exit("KZ3_ROW_NOT_FOUND")
lines[kz3_idx] = lines[kz3_idx].rstrip("\n") + ev + "\n"

# 2) Insert iter-log entry right after "## Iteration log" header line (anchor)
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
if hdr_idx is None:
    sys.exit("ITER_HDR_NOT_FOUND")
lines.insert(hdr_idx + 1, iter_entry)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("PATCH_OK")
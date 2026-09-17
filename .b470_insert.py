import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ev = " falsify 2026-09-08 (第212回, K-Z3 14時台帯初計測 run470A–C — 13時台 n 積み増し run469 (13:55, cold 3/60) 済の次の続行枠 (次 run ID run470), cron 実行時刻 14:04 が 14時台へ帯移行済みのため 13時台待機不可能、falsify 第88回/99回 precedent に従い現時刻帯 14時台帯初計測として実施, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:04:45–14:05:07 JST, 全 80/80 200, host load1 57.38 (14:05 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) — run470A cold 4/20 散発クラスタ (1.0909s/1.2693s/1.3442s/1.9256s) p50 134.8ms max 1925.6ms / run470B cold 単発 1/20 (1.2111s) p50 91.7ms max 1211.1ms / run470C cold 0/20 p50 129.7ms max 290.5ms, control (kotobase.net/signup) cold 0/20 p50 107.7ms max 203.3ms 完全静穏で control 分離成立、cold 群は search 側に局在。run470A 散発クラスタ 4/20 + B 単発 1/20 は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続 (heavy>=6/20 は 14時台帯初では非達 — run467A/468A 8/20/6/20 heavy 級の帯初再現は 14時台帯初 5/20 散発クラスタ+単発型に弱化、run469 散発減衰 3/60 → 帯初再上振れ 5/60 の帯初 1 窓上振れ型)。14時台 (9/8) 帯初計測 cold 5/60 ~8.3% — 12時台帯初 8/60 ~13.3% → 13時台帯初 8/60 ~13.3% → 14時台帯初 5/60 ~8.3% の帯初再上振れ継続 (帯移行時帯初に再上振れ → 帯内で散発減衰のパターン継続、日中帯セット間変動大続行、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。帯 n=1 セットのみで帯水準確定・機構判断には rank 追加 n を要する。)status 判定は rank に委ねる (rank 専門)。"

iter_entry = "\n- 2026-09-08: falsify 第212回。14:02 JST tick。HEAD a610982 = bench 第194回 (13:55, K-Z3 13時台 n-add run469 cold 3/60 — 13時台通算 17/180 ~9.4% 3セット; 前 HEAD c24e0c1 = falsify 第211回 run468) = remote net-kotobase/main 一致 (git fetch net-kotobase main + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第194回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 n 積み増し))。bench 第194回 NEXT は「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 13時台 n 積み増し続行, 次 run ID run470)」、本 tick は cron 実行時刻 14:04 が 14時台へ帯移行済みのため 13時台待機不可能、falsify 第88回/99回 precedent (現時刻帯で実施) に従い 14時台帯初計測 run470A–C を実施 (14時台 (9/8) 帯初 n=1 セット目)。live smoke 200 (/, /signup; pre-run 計測)。host load1 57.38 (14:05 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。K-Z3 14時台 run470A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 14:04:45–14:05:07 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 4/1/0 per 20 = 5/60 (~8.3%) — run470A cold 4/20 散発クラスタ (1.0909s/1.2693s/1.3442s/1.9256s) p50 134.8ms max 1925.6ms / run470B cold 単発 1/20 (1.2111s) p50 91.7ms max 1211.1ms / run470C cold 0/20 p50 129.7ms max 290.5ms, control (kotobase.net/signup) cold 0/20 p50 107.7ms max 203.3ms 完全静穏で control 分離成立、cold 群は search 側に局在。run470A 散発クラスタ 4/20 + B 単発 1/20 は C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」散発型継続 (heavy>=6/20 は 14時台帯初では非達、run469 散発減衰 3/60 → 帯初再上振れ 5/60 の帯初 1 窓上振れ型)。14時台 (9/8) 帯初計測 cold 5/60 ~8.3% — 12時台帯初 8/60 → 13時台帯初 8/60 → 14時台帯初 5/60 の帯初再上振れ継続 (帯移行時帯初に再上振れ → 帯内散発減衰のパターン継続、日中帯セット間変動大続行、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。帯 n=1 セットのみで帯水準・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L403 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run471)。"

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find L403 (accumulation row immediately before "## Iteration log")
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
if hdr_idx is None:
    sys.exit("ITER_HDR_NOT_FOUND")
l403_idx = hdr_idx - 1
lines[l403_idx] = lines[l403_idx].rstrip("\n") + ev + "\n"

# Insert iter-log entry right after "## Iteration log" header line
lines.insert(hdr_idx + 1, iter_entry)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

# scrub zero-width chars
raw = io.open(PATH, "r", encoding="utf-8").read()
raw2 = raw.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "").replace("\ufeff", "")
if raw2 != raw:
    io.open(PATH, "w", encoding="utf-8").write(raw2)
    print("PATCH_OK_ZWNBSP_SCRUBBED")
else:
    print("PATCH_OK")
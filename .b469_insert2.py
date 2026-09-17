import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ev = " bench 2026-09-08 (第194回, K-Z3 13時台 n 積み増し run469A–C — falsify 第211回 run468 (13:43, cold 6/60) 済の次の続行枠 (次 run ID は falsify 第211回 NEXT どおり run469), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:54:51–13:55:04 JST, 全 80/80 200, host load1 34.49 (13:54 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run469A cold 3/20 (0.9357s/1.1845s/1.2971s 散発配置) p50 133.9ms max 1297.1ms / run469B cold 0/20 p50 58.1ms max 146.9ms / run469C cold 0/20 p50 52.4ms max 187.2ms, control (kotobase.net/signup) cold 0/20 p50 53.0ms max 255.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。run469A 散発 3/20 は B/C 0/20 + control 0/20 で即消失し falsify run468A heavy 6/20 (13:43) の 12 分後散発減衰 (6/20 → 3/20) で「帯内 1 窓即消失」散発型継続 (heavy>=6/20 の帯内持続は run467A 8/20 → run468A 6/20 の 2 セットで弱く支持されるも 3 セット目で散発減衰、帯水準としての heavy 持続性は n 追加要)。13時台 (9/8) 通算 = run467 (8/60, 帯初) + falsify run468 (6/60) + 本 tick run469 (3/60) = 17/180 (~9.4%) の 3 セット中位〜高位帯候補 — 帯初/2 セット目の heavy 上振れ (8/60 → 6/60) から 3 セット目で散発減衰 (3/60)、日中帯セット間変動大続行 (12時台帯初 8/60 → 帯内減衰の同型パターン、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"

iter_entry = "\n- 2026-09-08: bench 第194回。13:55 JST tick。HEAD c24e0c1 = falsify 第211回 (13:48, K-Z3 13時台 n-add run468 cold 6/60 — orphaned .b468 scratch 採用; 前 HEAD adc3f34 = rank 第209回) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖)。本 tick は rank 第209回 NEXT「K-Z3 13時台 n-add run468」の枠として開始したが、作業中に sibling falsify 第211回が orphaned .b468 scratch (13:42–13:43) を検証・採用して run468 (cold 6/60, 13:43 計測) として commit (c24e0c1) 済みのため、falsify 第211回 NEXT「次 run ID は run469」に従い run469A–C を 13時台 n 積み増しとして実施（13時台 3 セット目、falsify run468 完了 ~11 分後の独立計測）。live smoke 200 (/, /signup; pre-run 計測) + 本 tick 実測 search.kotobase.net/search 200 / kotobase.net/signup 200。host load1 34.49 (13:54 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。K-Z3 13時台 run469A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 13:54:51–13:55:04 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) — run469A cold 3/20 (0.9357s/1.1845s/1.2971s 散発配置) p50 133.9ms max 1297.1ms / run469B cold 0/20 p50 58.1ms max 146.9ms / run469C cold 0/20 p50 52.4ms max 187.2ms, control (kotobase.net/signup) cold 0/20 p50 53.0ms max 255.8ms 完全静穏で control 分離成立、cold 群は search 側に局在。run469A 散発 3/20 は B/C 0/20 + control 0/20 で即消失し falsify run468A heavy 6/20 (13:43) の 12 分後散発減衰 (6/20 → 3/20) で「帯内 1 窓即消失」散発型継続 (heavy>=6/20 の帯内持続は run467A 8/20 → run468A 6/20 の 2 セットで弱く支持されるも 3 セット目で散発減衰)。13時台 (9/8) 通算 = run467 (8/60, 帯初) + falsify run468 (6/60) + 本 tick run469 (3/60) = 17/180 (~9.4%) の 3 セット中位〜高位帯候補 — 帯初/2 セット目の heavy 上振れ (8/60 → 6/60) から 3 セット目で散発減衰 (3/60)、日中帯セット間変動大続行 (12時台帯初 8/60 → 帯内減衰の同型パターン、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (run468 追記行の末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 13時台 n 積み増し続行、次 run ID は run470 使用)。\n"

with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1) Locate Iteration log header
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
if hdr_idx is None:
    sys.exit("ITER_HDR_NOT_FOUND")

# 2) Append evidence to the row just before the Iteration log header (line 403 = run468 evidence tail)
ev_row = hdr_idx - 1
lines[ev_row] = lines[ev_row].rstrip("\n") + ev + "\n"

# 3) Insert iter-log entry right after the header
lines.insert(hdr_idx + 1, iter_entry)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("PATCH_OK ev_row=%d hdr=%d" % (ev_row + 1, hdr_idx + 1))
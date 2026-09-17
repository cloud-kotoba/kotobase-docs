#!/usr/bin/env python3
# falsify 第168回: append run393 evidence to K-Z3 L279 END + insert iter-log entry (newest-first)
EN = "\u2013"  # en-dash
path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()

# 1) append evidence to L279
ev = (
 " falsify 2026-09-07 (第168回, K-Z3 20時台 n 積み増し run393A" + EN +
 "C" + EN + "C 追加 n-add (run393 は iter-log bench-175 NEXT\u300c次 run ID は run393\u300dの枠, 衝突なし確認), 同測定法 "
 "n=20 " + "\u00d7" + " 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint "
 "search.kotobase.net/search?q=test, 20:19:18" + EN + "20:19:40 JST, 全 80/80 200, host load1 9.17 "
 "(20:19 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 " + EN +
 " curl + python stats のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) " + EN +
 " run393A cold 2/20 散発 (1.0469s pos2 / 1.6430s pos5) p50 66.9ms max 1.643s / run393B cold 0/20 "
 "p50 53.9ms max 141.5ms / run393C cold 0/20 p50 60.1ms max 154.6ms, control (kotobase.net/signup) "
 "cold 0/20 p50 43.8ms max 409.3ms 完全静穏 (max 409ms は閾値内 1 件の上振れ) で control 分離成立、" +
 EN + "cold 群は search 側に局在。run393A 散発 2/20 は B/C 0/40 + control 0/20 で即消失し\u300c帯内 1 窓即消失\u300d散発クラスタ型継続 " + EN +
 " bench run392A heavy 6/20 (20:14) の 5 分後散発減弱で heavy 再達せず (run392A heavy は 1 窓非持続)。20時台 (9/7) 通算 = "
 "bench run392 (7/60) + 本 tick run393 (2/60) = 9/120 (~7.5%) の 2 セット中位帯候補 " + EN + " 19時台 (~8.0%) と同水準の帯横断継続 "
 "(日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。status 判定は rank に委ねる (rank 専門)。"
)
lines = s.split("\n")
assert lines[278].startswith("| K-Z3 |"), "L279 not K-Z3 row"
lines[278] = lines[278] + ev
s = "\n".join(lines)

# 2) insert iter-log entry as new line right after "## Iteration log" header (newest-first)
ilog = (
 "- 2026-09-07: falsify 第168回。20:19 JST tick。HEAD d84bf4a = bench 第175回 (20:09, K-Z3 20時台帯初 "
 "run392 cold 7/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD "
 "のため fetch 系で取込)。※pre-run monitor NEXT\u300cK-Z3 深夜帯 23時台 n 積み増し継続\u300dは stale (rank 第90回帯 artifact) " + EN +
 " true progressive NEXT は iter-log HEAD (bench 第175回)\u300c委ねる (rank 指定優先; falsify/bench フォールバックは "
 "K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run393 使用\u300dの run393 枠を本 tick 実施 (20時台 n-add, "
 "run392 帯初 7/60 の追加)). K-Z3 20時台 run393A" + EN + "C 実測 (同測定法 n=20 " + "\u00d7" + " 3 + landing control, 別接続 curl, "
 "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 20:19:18" + EN + "20:19:40 JST, "
 "全 80/80 200, secret 不含 " + EN + " curl + python stats のみ): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) " + EN +
 " run393A cold 2/20 散発 (1.0469s pos2 / 1.6430s pos5) p50 66.9ms / run393B 0/20 p50 53.9ms / run393C 0/20 "
 "p50 60.1ms, control 0/20 p50 43.8ms 完全静穏分離成立。run393A 散発は B/C+control 0/40 即消失で run392A heavy 6/20 "
 "(20:14) の 5 分後散発減弱 " + EN + " 20時台通算 9/120 (~7.5%) 中位帯候補。status 判定は rank に委ねる (rank 専門)。"
 "secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは "
 "K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run394 使用 " + EN + " " + "\u203b" + "sibling falsify/cosientist 分は同一帯 "
 "independent 計測のため rank 判定の取込対象)。"
)
lines = s.split("\n")
hdr_idx = None
for i,l in enumerate(lines):
    if l.strip() == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "iterlog header not found"
lines.insert(hdr_idx + 1, ilog)
s = "\n".join(lines)

open(path, "w", encoding="utf-8").write(s)
print("EDITED OK. L279 len:", len(lines[278]))
print("iter-log lines after header:", lines[hdr_idx+1][:60])
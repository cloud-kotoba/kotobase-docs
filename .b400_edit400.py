path = "query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

kz3_idx = None
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |") and kz3_idx is None:
        kz3_idx = i
    if ln.startswith("## Iteration log") and ilog_idx is None:
        ilog_idx = i
assert kz3_idx is not None and ilog_idx is not None, "anchors not found"

EVID_TAIL = (
    " bench 2026-09-07 (第181回, K-Z3 21hr n-add run400A-C: 同測定法 n=20 x 3 + landing control, "
    "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "21:55:45-21:56:02 JST, 全 80/80 200, secret 不含): "
    "cold(>=0.5s) 5/1/1 per window = 7/60 (~11.7%) - run400A 散発クラスタ 5/20 (deep 2.4605s 含む) p50 72.2ms, "
    "run400B 単発 1/20 (0.9867s) p50 55.8ms, run400C 単発 1/20 (1.6021s) p50 50.7ms; "
    "control (kotobase.net/signup) cold 0/20 p50 58.0ms max 340.5ms 完全静穏で control 分離成立, "
    "cold 群は search 側に局在。run400A 散発クラスタ 5/20 は B/C 0/40 即消失で「帯内 1 窓即消失」型継続 "
    "(heavy>=6/20 は再達せず)。21時台通算 = falsify-run397 2/60 + bench178-run397 3/60 + bench179-run398 6/60 "
    "+ bench180-run399 1/60 + run400 7/60 = 19/300 (~6.3%) 5 セット中位帯候補 - 20時台 (20/360 ~5.6%) と同水準の帯横断継続。"
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
)
lines[kz3_idx] = lines[kz3_idx].rstrip("\n") + EVID_TAIL + "\n"

ILOG = (
    "- 2026-09-07: bench 第181回。21:52 JST tick。HEAD 44ac3a7 = bench 第180回 (21:40, K-Z3 21hr n-add run399 1/60) "
    "= remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; "
    "terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。"
    "host load1 34.51 (21:52 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否 - 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) - true progressive NEXT は "
    "iter-log HEAD (bench 第180回, 21:40)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 21時台 n 積み増し続行、"
    "次 run ID は run400 使用)」の run400 枠を本 tick 実施 (.b400 既存なし=衝突なし確認, 21時台 5 セット目)。"
    "K-Z3 21時台 run400A-C 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 21:55:45-21:56:02 JST, 全 80/80 200, secret 不含): "
    "cold(>=0.5s) 5/1/1 per 20 = 7/60 (~11.7%) - run400A 散発クラスタ 5/20 (deep 2.4605s 含む) p50 72.2ms, "
    "run400B 単発 1/20 (0.9867s) p50 55.8ms, run400C 単発 1/20 (1.6021s) p50 50.7ms, "
    "control (kotobase.net/signup) cold 0/20 p50 58.0ms max 340.5ms 完全静穏で control 分離成立, cold 群 search 側に局在。"
    "run400A 散発クラスタ 5/20 は B/C 0/40 即消失で「帯内 1 窓即消失」型継続 (heavy>=6/20 は再達せず)。"
    "21時台通算 = 19/300 (~6.3%) の 5 セット中位帯候補 - 20時台 (20/360 ~5.6%) と同水準の帯横断継続 "
    "(日中帯 traffic 依存説の夜帯低位方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。"
    "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。"
    "NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 21時台 n 積み増し続行、次 run ID は run401 使用)。"
)
lines.insert(ilog_idx + 1, ILOG)

with open(path, "w", encoding="utf-8") as f:
    f.write("".join(lines))
print("edited ok")
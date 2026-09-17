import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(P, encoding="utf-8", newline="").read()
assert "run641A-C" not in src, "run641 already present - collision, abort"

ev = "cosientist 2026-09-16 (第156回, K-Z3 14時台 n 積み増し run641A-C, 同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 14:13-14:23 JST, 全 80/80 200, 正 endpoint search.yataverse.com/search?q=test, host load1 33.38 (14:07 pre-tick monitor 実測) / 60.09 (14:12 pre-measure uptime 実測) / 29.71 (14:23 post-run uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 - curl + python3 stats のみ): cold(>=0.5s) 7/3/0 per 20 = 10/60 (~16.7%) - run641A cold 7/20 (冒頭 1-3番目連続 700.1-1041.5ms + 中盤以降散発 #7 891.1ms / #11 893.0ms / #13 1033.1ms / #19 1468.9ms, 分散配置) p50 183.2ms p95 1468.9ms / run641B cold 3/20 (中盤散発 #3 1196.9ms / #6 1326.0ms / #8 1376.8ms) p50 111.2ms / run641C cold 0/20 p50 75.8ms max 164.5ms, landing control (kotoba.cloud/, 同時刻, n=20, 全 200) cold 0/20 p50 106.9ms max 206.4ms 完全静穏で control 分離成立、cold 群は search 側に局在。14時台サンプルで中位水準 (~16.7%, 13時台 run640 ~16.7% と同水準の連続, 日中帯 traffic 依存パターンと整合)。rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (14時台) のため待機不可能につきフォールバック実施。run641 は 第155回 NEXT 指定 ID につき衝突なし。status 判定は rank に委ねる (rank 専門)。"

il = "- 2026-09-16: cosientist 第156回 (14:1x JST tick)。HEAD 6fc55f3 = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗のため不使用手順)。monitor: host load1 33.38 (14:07 pre-tick monitor 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), live smoke 301/301 (kotobase.net/ → 301, kotobase.net/signup → 301)。rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」につき本 tick 時刻 (14時台) のため 23時台待機不可能 — フォールバック (production HTTP 実測) で K-Z3 14時台 n 積み増し run641A-C を実施 (第155回 NEXT 指定 run ID run641, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 14:13-14:23 JST, 全 80/80 200): cold(>=0.5s) 10/60 (~16.7%) - A 7/20 冒頭 1-3番目連続 + 中盤散発 (700.1-1468.9ms) + B 3/20 中盤散発 (1196.9-1376.8ms) + C 0/20, control (kotoba.cloud/) 0/20 p50 106.9ms max 206.4ms 完全静穏で control 分離成立。14時台サンプルは中位水準 (13時台 run640 ~16.7% と同水準の連続)。evidence は本ファイル末尾に追記済み (第153-155回前例のファイル末尾追記方式)。status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続, 次 run ID は run642 使用)。secret 不含 (curl + python3 stats のみ)。"

if not src.endswith("\n"):
    src += "\n"
out = src + ev + "\n" + il + "\n"
io.open(P, "w", encoding="utf-8", newline="").write(out)
print("appended", len(out) - len(src), "chars")

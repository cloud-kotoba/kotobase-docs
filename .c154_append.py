import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")

ev_line = ("cosientist 2026-09-15 (第154回, K-Z3 13時台 n 積み増し run631A-C, 同測定法 n=20 x3 + landing control, "
"別接続 curl, Tokyo, 13:44:36-13:44:46 JST, 全 80/80 200, 正 endpoint search.yataverse.com/search?q=test 直接計測 "
"(旧 search.kotobase.net/search は 301 読替のため本 tick 冒頭の無効 301 セット run625 1 本は不採用注記), "
"host load1 12.51-12.06 (13:41/13:44 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, "
"secret 不含 - curl + python3 stats のみ): cold(>=0.5s) 0/60 完全静穏 - run631A cold 0/20 p50 51.5ms max 154.8ms / "
"run631B cold 0/20 p50 56.5ms max 154.7ms / run631C cold 0/20 p50 65.7ms max 166.1ms, "
"landing control (kotoba.cloud/, 同時刻, n=20, 全 200) cold 0/20 p50 112.4ms max 168.7ms 完全静穏で control 分離成立 "
"(両群 cold 0 で分離判定は非適用)。13時台 (9/15) 帯 n=1 セット 0/60 完全静穏 - 同帯 9/7 通算 19/480 (~4.0%) 中位帯候補と同帯日次対比の K-Z4 材料。"
"run ID: fetch 後 grep run630/run631 = 0 確認済み (run629 まで使用) のため衝突なし。"
"status 判定は rank に委ねる (rank 専門)。")

it_line = ("- 2026-09-15: cosientist 第154回 (13:41 JST tick)。HEAD f9cbe29 = fetch 後 net-kotobase/main 先端一致 "
"(worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗のため "
"fetch + rev-parse 比較手順; terminal foreground stdout 空 = 既知のため状態確認はファイル書出経由)。monitor: host load1 16.04 "
"(13:41 pre-tick 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), live smoke 301/301 (kotobase.net/ と /signup, "
"pre-run monitor 計測の記録どおり)。rank NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は本 tick 時刻 (13時台) のため待機不可能 — "
"フォールバック (production HTTP 実測) で K-Z3 13時台 n 積み増しを実施。本 tick 冒頭の run625A-C 計測は旧 endpoint "
"search.kotobase.net/search の 301 応答による無効セット (search 0/20 200) で不採用 — 正 endpoint search.yataverse.com/search?q=test を "
"確認後 有効再実施し run631 として記録 (同測定法 n=20 x3 + landing control, 別接続 curl, Tokyo, 13:44:36-13:44:46 JST, 全 80/80 200, "
"control kotoba.cloud/): cold(>=0.5s) 0/60 完全静穏 - A p50 51.5ms max 154.8ms / B 56.5ms max 154.7ms / C 65.7ms max 166.1ms, "
"control 0/20 p50 112.4ms max 168.7ms 完全静穏で control 分離成立 (両群 cold 0 で分離判定は非適用)。13時台 (9/15) 帯 n=1 セット "
"0/60 完全静穏は K-Z4 日次変動材料 (同帯 9/7 通算 ~4.0% 中位帯候補 vs 本日 0%)。run ID 衝突なし (fetch 後 grep run631=0 確認 — "
"run625 は本 tick 無効 301 セットとして消費, run630 は未使用のため採用 ID は run631)。evidence は K-Z3 仮説行に追記済み。"
"status 判定は rank に委ねる (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 13時台 n 積み増し継続, "
"次 run ID は run632 使用)。secret 不含 (curl + python3 stats のみ)。")

appended_ev = 0
# K-Z3 evidence rows are at lines 281 and 283 (1-indexed); evidence column is the 4th,
# row ends with '| open | <evidence>' style — check actual endings: line 281 ends with '(rank 専門)。' etc.
# Locate the two table rows and append ev_line to the LAST one (L283, which holds recent evidence).
idxs = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 | worker |")]
if idxs:
    i = idxs[-1]
    lines[i] = lines[i].rstrip() + " " + ev_line
    appended_ev = 1

final = []
appended_it = 0
for ln in lines:
    final.append(ln)
    if ln.strip() == "## Iteration log":
        final.append(it_line)
        appended_it += 1

assert appended_ev == 1, f"ev={appended_ev}"
assert appended_it == 1, f"it={appended_it}"

with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(final))
print("ok ev=1 it=1")

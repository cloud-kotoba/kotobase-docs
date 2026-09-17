# falsify 218 run488: append evidence to K-Z3 row end + iter-log insert
P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(P, encoding="utf-8") as f:
    text = f.read()
lines = text.split("\n")

ev = " falsify 2026-09-08 (第218回, K-Z3 17時台 n-add run488A-C, 同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 18:00-18:02 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 45.78-57.88 (17:58-18:00 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%). run488A cold 5/20 散発クラスタ (1.0506/1.1070/1.2674/1.2974/2.1620s) p50 110.7ms / run488B 単発 1/20 (1.4871s) p50 109.8ms / run488C cold 0/20 p50 55.0ms max 158.5ms. landing control (kotobase.net/signup) cold 0/20 p50 57.0ms max 479.4ms 完全静穏で control 分離成立, cold 群 search 側局在, cold 6 件閾値決定的。17時台 (9/8) 通算 = run485 (6/60) + run486 (6/60) + run487 (10/60) + 本 tick run488 (6/60) = 28/240 (~11.7%) の 4 セット日中帯高位継続, 帯内振幅 6-10/60 (heavy は run487A 7/20 のみ), traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)。"

kz3_idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        kz3_idx = i
        break
assert kz3_idx is not None
lines[kz3_idx] = lines[kz3_idx] + ev

ilog_idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        ilog_idx = i
        break
assert ilog_idx is not None

entry = "- 2026-09-08: falsify 第218回。17:58 JST tick。HEAD 83e5024 = bench 第212回 (17:44, K-Z3 17時台 run487 cold 10/60) = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のためファイル経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact 前例多) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第212回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 17時台 n 積み増し続行, 次 run ID は run488))。host load1 47.78 (17:58 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。live smoke 200 (/, /signup; pre-run)。K-Z3 17時台 run488A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, Tokyo, 18:00-18:02 JST, 全 80/80 200): cold(>=0.5s) 5/1/0 per 20 = 6/60 (~10.0%) — run488A 散発クラスタ 5/20 / run488B 単発 1/20 / run488C 0/20, landing control cold 0/20 完全静穏で control 分離成立、cold 群 search 側局在。17時台 (9/8) 通算 = run485 (6/60) + run486 (6/60) + run487 (10/60) + 本 tick run488 (6/60) = 28/240 (~11.7%) の 4 セット日中帯高位継続。status 判定は rank 専門。secret は一切記録せず。詳細は K-Z3 evidence 欄に追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run489)。"
lines.insert(ilog_idx+1, entry)

with open(P, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("APPEND_DONE")
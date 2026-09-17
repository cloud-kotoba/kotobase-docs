# bench 212: insert iter-log entry right after "## Iteration log" header
F = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
ENT = "- 2026-09-08: bench 第212回. 17:44 JST tick. HEAD a601bd5 = bench 第211回 (17時台 K-Z3 run486 cold 6/60; NEXT 委ねる → run487) = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact 前例) — true progressive NEXT は iter-log HEAD 連鎖 (bench 第211回 NEXT 委ねる → フォールバック K-Z3 現在時刻帯 17時台 n 積み増し続行, 次 run ID は run487))。host load1 47.78 (17:44 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。live smoke 200 (/, /signup; pre-run)。K-Z3 17時台 run487A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 17:44 窓, 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 7/1/2 per 20 = 10/60 (~16.7%) — run487A heavy 散発クラスタ 7/20 (0.589–2.309s) / run487B 単発 1/20 (2.124s) / run487C 2/20 (1.532/1.724s), control (kotobase.net/signup) cold 0/20 p50 53.9ms max 393.7ms 完全静穏で control 分離成立、cold 群 search 側局在。17時台 (9/8) 通算 = falsify run485 (6/60 帯初) + bench run486 (6/60) + 本 tick run487 (10/60) = 22/180 (~12.2%) の 3 セット中〜高位帯候補 — 16時台 (27/360 ~7.5%) から 17時台への高位帯確定方向、traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank 専門。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 17時台 n 積み増し続行, 次 run ID は run488)。\n"

hd = "## Iteration log\n"
with open(F, "r", encoding="utf-8") as f:
    content = f.read()
assert hd in content, "iter-log header not found"
content = content.replace(hd, hd + ENT, 1)
with open(F, "w", encoding="utf-8") as f:
    f.write(content)
print("ITER_LOG_INSERTED")
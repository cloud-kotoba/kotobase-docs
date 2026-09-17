#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding="utf-8").read().split("\n")
# find "## Iteration log" line index
hdr=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        hdr=i; break
assert hdr is not None
entry=("- 2026-09-07: **falsify 第160回**。12:11 JST tick。HEAD 74fba58 = bench 第147回 (12:01, K-Z3 11時台 run344 cold 5/60) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み, terminal foreground 出力不可=知己のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 ~27 (12:11 uptime 実測, gate 7.5 超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は bench 第147回 (Iteration log 先頭, 12:01)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 12時台 n 積み増し続行, 次 run ID は run345 使用)」の run345 枠を本 tick 実施 (12時台帯初, 11時台 run339..344 済み 6 セット後の積み増し続行)。K-Z3 12時台 帯初計測 run345A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 12:17:46–12:18:20 JST, 全 80/80 200, secret 不含 — curl のみ): cold(>=0.5s) 6/1/2 per 20 = 9/60 (~15%) — run345A cold 6/20 (1.1966/0.9263/1.0876/1.2746/1.6165/0.5133s 散発クラスタ) p50 164.6ms / run345B cold 単発 1/20 (1.3562s) p50 177.2ms / run345C cold 2/20 (0.6139/1.708s) p50 149.3ms, control (kotobase.net/signup) cold 1/20 (0.5121s 閾値境界値) p50 130.6ms — control 境界 1 件で borderline not-separated 傾向だが search cold 9 件は 0.51–1.71s で control 0.5121s 境界と逆方向の magnitude 分離弱成立 (search 側 deep cold 1.6–1.7s 実在)。run345A cold 6/20 は heavy (>=6/20) 閾値に再達する初候補 (run341A 6/20 弱候補の再上振れ, run331A 9/20 heavy 型の強弱再出現系) で 12時台帯初計測として cold 9/60 ~15% の高位帯初期サンプル — B/C 0/60 で「帯内 1 窓即消失」型は維持 (heavy>=6/20 の持続性は帯内追加 n で確認)。12時台 (9/7) 通算 = 9/60 (~15%) の 1 セット帯初高位候補。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 12時台 n 積み増し続行、次 run ID は run346 使用)")
lines.insert(hdr+1, entry)
open(p,"w",encoding="utf-8").write("\n".join(lines))
print("inserted at line", hdr+2, "new total", len(lines))
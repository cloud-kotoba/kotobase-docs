#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(p,encoding="utf-8").read()
lines=s.split("\n")
idx=278
ADDS = (" falsify 2026-09-07 (第160回, K-Z3 12時台帯初計測 run345A–C — bench 第147回 (12:01) の NEXT 委ねる枠 (フォールバックは K-Z3 現在時刻帯 12時台 n 積み増し続行, 次 run ID run345) の run345 枠として実施, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 12:17:46–12:18:20 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 53.60→67.69 (12:17–12:18 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 6/1/2 per 20 = 9/60 (~15%) — run345A cold 6/20 (1.1966s/0.9263s/1.0876s/1.2746s/1.6165s/0.5133s 散発クラスタ) p50 164.6ms / run345B cold 単発 1/20 (1.3562s) p50 177.2ms / run345C cold 2/20 (0.6139s/1.708s) p50 149.3ms, control (kotobase.net/signup) cold 1/20 (0.5121s 閾値境界値) p50 130.6ms — control 境界 1 件で borderline not-separated 傾向だが search cold 9 件は 0.51–1.71s で control 0.5121s 境界と逆方向の magnitude 分離弱成立 (search 側 deep cold 1.6–1.7s 実在)。run345A cold 6/20 は heavy (>=6/20) 閾値に再達する初候補 (run341A 6/20 弱候補の再上振れ, run331A 9/20 heavy 型の強弱再出現系) で 12時台帯初計測として cold 9/60 ~15% の高位帯初期サンプル — ただし B/C 0/60 で「帯内 1 窓即消失」型は維持 (heavy>=6/20 の持続性は帯内追加 n で確認)。12時台 (9/7) 通算 = 本 tick run345 (9/60) = 9/60 (~15%) の 1 セット帯初高位候補。status 判定は rank に委ねる (rank 専門)。")
lines[idx]=lines[idx]+ADDS
open(p,"w",encoding="utf-8").write("\n".join(lines))
print("appended. new L279 len", len(lines[idx]))
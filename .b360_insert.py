#!/usr/bin/env python3
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(p,encoding="utf-8").read()
anchor = "14時台帯初の初候補 (run345A/347A/341A の 12/11時台 heavy 再出現系の後続, run331A 9/20 heavy 型の 14時台再出現) — B/C 0/60 + control 0/20 で「帯内 1 窓即消失」型維持を示す (heavy の持続性は帯内追加 n で確認)。14時台 (9/7) 帯初計測 = 7/60 (~11.7%) の 1 セット日中高位帯初期サンプル。status 判定は rank に委ねる (rank 専門)。"
add = " bench 2026-09-07 (第156回, K-Z3 14時台 n 積み増し run360A–C — bench 第155回 (iter-log 14:16) NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行、次 run ID は run360 使用)」の run360 枠として実施, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 14:25:55–14:26:10 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 75.36→69.37 (14:25/14:26 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) — run360A cold 単発 1.1969s p50 68.9ms max 1196.9ms / run360B cold 0/20 p50 93.2ms max 244.4ms / run360C cold 0/20 p50 76.4ms max 251.8ms, control (kotobase.net/signup) cold 0/20 p50 126.4ms max 250.1ms 完全静穏で control 分離成立、cold 群は search 側に局在。run360A cold 単発 1/20 は B/C 0/20 + control 0/20 で即消失し「帯内 1 窓即消失」型継続 — run359A cold 6/20 heavy (14:16) の 9 分後 1/20 への減弱 (heavy>=6/20 は再達せず, run331A 9/20 heavy 型の帯水準持続性は引き続き再現未確認)。14時台 (9/7) 通算 = run359 (7/60) + run360 (1/60) = 8/120 (~6.7%) の 2 セット日中高位帯候補 (帯初 heavy から 1/60 単発への即減弱で帯内 1 窓即消失パターン維持, K-Z3 traffic 依存説の日中帯方向支持継続)。status 判定は rank に委ねる (rank 専門)。"
n = s.count(anchor)
print("anchor occurrences:", n)
if n != 1:
    raise SystemExit("anchor not unique: %d" % n)
s2 = s.replace(anchor, anchor + add)
io.open(p,"w",encoding="utf-8").write(s2)
print("inserted. new len delta:", len(s2)-len(s))
#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(p,encoding="utf-8").read()
lines=s.split("\n")
idx=278
ADDS = (" falsify 2026-09-07 (第161回, K-Z3 12時台 n 積み増し run347A–C — rank 第150回 (8e8f56f, 12:32) ket NEXT「K-Z3 12時台 n-add, 次 run ID run347」の run347 枠として実施, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 12:37:02–12:37:19 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 36.89→39.99 (12:37 uptime 実測, gate 7.5 超出) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 6/0/0 per 20 = 6/60 (~10%) — run347A cold 6/20 (1.2721s/0.9677s/1.9807s/1.3052s/0.9602s/1.2565s 散発クラスタ) p50 99.6ms / run347B cold 0/20 p50 60.8ms max 106.3ms / run347C cold 0/20 p50 85.7ms max 180.5ms, control (kotobase.net/signup) cold 0/20 p50 84.4ms max 470.1ms 完全静穏で control 分離成立、cold 群は search 側に局在。run347A cold 6/20 は heavy (>=6/20) クラスタで、12時台帯内では run345A 6/20 に続く 2 回目の heavy 再出現 (run346 3/60 散発単発の直後再上振れ — run331A 9/20 heavy 型の 12時台再出現系, 帯内 heavy の再発は「帯内 1 窓即消失」型を越える帯水準での持続性を示唆)。runA 6/20 は B/C 0/20 + control 0/20 で即消失 (heavy>=6/20 の帯内維持は B/C 0/60 で未確認)。12時台 (9/7) 通算 = run345 9/60 + run346 3/60 + 本 tick 6/20 = 18/180 (~10%) の 3 セット中〜高位帯候補 — 12時台は日中帯で cold 濃度 10% 級の high-band 候補として帯水準が立ち始めた (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。ただし帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。")
lines[idx]=lines[idx]+ADDS
open(p,"w",encoding="utf-8").write("\n".join(lines))
print("appended. new L279 len", len(lines[idx]))
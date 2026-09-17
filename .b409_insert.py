#!/usr/bin/env python3
# Append falsify 179 K-Z3 run409 evidence to END of L279 (K-Z3 hypothesis row).
# evidence append-only; status rewrite is rank's job. no secrets.
path="query-cosientist.md"
txt=open(path,encoding="utf-8").read()
ev=(" falsify 2026-09-08 (第179回, K-Z3 0時台(深夜帯) n 積み増し run409A-C "
"--- iter-log HEAD (rank 第174回, f650bf8) NEXT\u300cK-Z3 0hr n-add run409\u300d の run409 枠実施, "
"同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 00:47:03-00:47:22 JST, 全 80/80 200, "
"正 endpoint search.kotobase.net/search?q=test, host load1 ~9.6 (00:47 uptime 実測, gate 7.5 超過) "
"は production HTTP 実測のため gate 外, secret 不含 - curl + python stats のみ): "
"cold(>=0.5s) 10/0/0 per 20 = 10/60 (~16.7%) "
"--- run409A cold 10/20 heavy 散発クラスタ (0.8866/0.9476/0.9544/1.0569/1.0940/1.4836/1.5599/1.7183/1.8212/1.9454s "
"--- deep ~0.89-1.95s 冒頭+中盤+末広がり, warm 群 0.042-0.26s) p50 141.9ms max 1.9454s "
"/ run409B cold 0/20 p50 45.2ms max 141.1ms / run409C cold 0/20 p50 48.0ms max 140.6ms, "
"control (kotobase.net/signup) cold 0/20 p50 44.5ms max 438.9ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
"run409A heavy 10/20 は B/C 0/40 + control 0/20 即消失で\u300c帯内 1 窓即消失\u300d散発型の最大級単一窓継続 "
"(0時台 heavy>=6/20 を初達成 - run407A 4/20 / run408A 4/20 から run409A 10/20 へ増大, "
"深夜帯 traffic 最低帯での heavy クラスタ出現は K-Z3 traffic 依存説への反証材料を継続)。"
"0時台 (9/8) 通算 = run407 (4/60) + run408 (4/60) + 本 tick run409 (10/60) = 18/180 (~10.0%) の 3 セット "
"--- 初期 2 セット ~6.7% 中位から run409A heavy により ~10.0% 高位候補へ上昇 (23時台 9/7 ~11.3% と同水準、22時台 ~14.2% との中位対比)。"
"深夜帯 traffic 最低での cold 3 セット連続出現 + heavy クラスタ再達は夜帯 traffic 遷移説が深夜帯 0時台まで継続する可能性を示唆、純 traffic 依存説への反証継続。"
"帯 n=3 セットで帯水準確定・機構判断は rank 追加 n 待ち。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。")
ev=ev.replace("\u200b","").replace("\u200c","").replace("\u200d","").replace("\ufeff","")
assert "#####" not in ev, "illegal token"
lines=txt.split("\n")
# ensure L279 (index 278) still the K-Z3 row
assert lines[278].startswith("| K-Z3 |"), "L279 no longer K-Z3 row"
lines[278]=lines[278]+ev
open(path,"w",encoding="utf-8").write("\n".join(lines))
print("appended, L279 len now=",len(lines[278]))
print("occ K-Z3 =", txt.count("| K-Z3 |"))
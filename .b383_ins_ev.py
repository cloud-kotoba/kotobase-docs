#!/usr/bin/env python3
# Append run383 evidence to K-Z3 evidence row (L279), anchored on unique tail.
fn='query-cosientist.md'
txt=open(fn,encoding='utf-8').read()
anchor="の 2 セット帯初候補,,帯水準確定は rank 追加 n 要る)。status 判定は rank に委ねる (rank 専門)。"
add=" bench 2026-09-07 (第169回, K-Z3 18時台 n-add run383A–C, 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 18:27:42–18:28:00 JST, 全 80/80 200, host load1 42.96→48.38 (pre/end uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): cold(>=0.5s) 3/3/1 per 20 = 7/60 (~11.7%) — run383A cold 3/20 (1.2473s/1.1567s/0.9991s 散発) p50 0.118s max 1.247s / run383B cold 3/20 (0.5267s/1.2953s/1.2065s 散発, 0.5267s は境界値) p50 0.078s max 1.295s / run383C cold 単発 1/20 (1.4898s 散発) p50 0.078s max 1.490s, control (kotobase.net/signup) cold 0/20 p50 0.080s max 0.318s 完全静穏で control 分離成立、cold 群は search 側に局在。run383A/B 各散発 (3/20) + C 単発は control 0/20 で即消失し「帯内 1 窓即消失」散発単発/ペア型の延長 (heavy>=6/20 は再達せず) — 18時台 (9/7) 通算 = run381 (2/60) + run382 (4/60) + 本 tick run383 (7/60) = 13/180 (~7.2%) の 3 セット中位帯候補 (17時台 27/360 ~7.5% と同水準の帯横断継続, 日中帯 traffic 依存説の方向支持) — host load 高騰 (43–48) の p50 上振れは control 0/20 完全静穏で cold 濃度 7/60 は閾値決定的, control 分離成立で機構判定としては clean。status 判定は rank に委ねる (rank 専門)。"
assert txt.count(anchor)==1, "anchor not unique: %d"%txt.count(anchor)
new=txt.replace(anchor, anchor+add)
open(fn,'w',encoding='utf-8').write(new)
print("inserted run383 evidence ok")
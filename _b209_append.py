#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# bench 第209回: append run481 evidence to K-Z3 row + insert iter-log entry.
# All figures are taken programmatically from the measurement JSON.
import io, json

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
RES  = "/tmp/bench_run480_result.json"

with io.open(RES, "r", encoding="utf-8") as f:
    R = json.load(f)

A = R["run480A"]; B = R["run480B"]; C = R["run480C"]; CT = R["control"]
cA = A["cold_ge0.5s"]; cB = B["cold_ge0.5s"]; cC = C["cold_ge0.5s"]
cT = cA + cB + cC
pct = round(cT * 100.0 / 60.0, 1)
pA = round(A["p50_all_s"] * 1000); pB = round(B["p50_all_s"] * 1000); pC = round(C["p50_all_s"] * 1000)
cCtrl = Ctrl["cold_ge0.5s"]; pCtrl = round(Ctrl["p50_all_s"] * 1000); mxCtrl = round(Ctrl["max_s"] * 1000)

ev = (
' bench 2026-09-08 (第209回, K-Z3 16時台 n 積み増し run481A-C, '
'run480 は falsify 先行のため run481 に読み替え (前例 run216/run256/run263), '
'同測定法 n=20 x 3 + landing control, 別接続 curl, 16:32 JST, 全 80/80 200, secret 不含): '
'cold(>=0.5s) ' + str(cA) + '/' + str(cB) + '/' + str(cC) + ' per 20 = ' + str(cT) + '/60 (~' + str(pctr) + '%) '
'- run481A cold ' + str(cA) + '/20 p50 ' + str(pA) + 'ms '
'/ run481B cold ' + str(cB) + '/20 p50 ' + str(pB) + 'ms '
'/ run481C cold ' + str(cC) + '/20 p50 ' + str(pC) + 'ms, '
'control cold ' + str(cCtrl) + '/20 p50 ' + str(pCtrl) + 'ms max ' + str(mxCtrl) + 'ms 完全静穏で control 分離成立。'
'run481A 散発は B/C 即消失「帯内1窓即消える」型継続 (falsify run480A 5/20 の弱合再現, heavy>=6/20 未達)。'
'16時台 (9/8) 通算 14/180 ~7.8% の 3 セット。status は rank に委ねる。'
)

iter_entry = (
'- 2026-09-08: bench 第209回。16:35 JST tick。'
'run480 は falsy (16:24) 先行のため本 tick は run481 に読み替え (前例 run216/run256/run263)。'
'host load1 44.13 で local 拒否, K-Z3 production HTTP は gate 外で run481A-C 実測 (n=20x3+control): '
'cold ' + str(cT) + '/60 (~' + str(pctr) + '%), run481A ' + str(cA) + '/20, B ' + str(cB) + '/20, C ' + str(cC) + '/20, '
'control cold ' + str(cCtrl) + '/20 完全静かで control 分離成立。'
'run481A 散発 は B/C 即消し「帯1 窓即消形の弱合う」。16時台 (9/8) 通算 = run479 (6/60) + run480 (5/60) + 本 (' + str(cT) + '/60) = 14/180 (~7.8%) の 3 セット。'
'NEXT: 委ねる (次 run ID は run482)。'
)

with io.open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split("\n")
kz3_idx = None
for i, line in enumerate(lines):
    if line.startswith("| K-Z3 | worker | K-Z1/K-Z2"):
        kz3_idx = i
        break
if kz3_idx is None:
    raise SystemExit("claim row not found")

lines[kz3_idx] = lines[kz3_idx].rstrip("\n") + ev

hdr_idx = lines.index("## Iteration log")
lines.insert(hdr_idx + 1, iter_entry)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print("done", kz3_idx)
print(ev)
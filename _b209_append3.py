#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, json

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
RES  = "/tmp/bench_run480_result.json"

with io.open(RES, "r", encoding="utf-8") as f:
    R = json.load(f)

A = R["run480A"]; B = R["run480B"]; C = R["run480C"]; ctl = R["control"]
cA = A["cold_ge0.5s"]; cB = B["cold_ge0.5s"]; cC = C["cold_ge0.5s"]
cT = cA + cB + cC
pct = round(cT * 100.0 / 60.0, 1)
pA = round(A["p50_all_s"] * 1000); pB = round(B["p50_all_s"] * 1000); pC = round(C["p50_all_s"] * 1000)
cCtrl = ctl["cold_ge0.5s"]; pCtrl = round(ctl["p50_all_s"] * 1000); mxCtrl = round(ctl["max_s"] * 1000)

# 16時台 (9/8) band totals: run479 (6/60, band no) + run480 (5/60) + this run481
r479 = 6
r480 = 5
band_cold = r479 + r480 + cT
band_den = 180
pct_band = round(band_cold * 100.0 / band_den, 1)

ev = (
' bench 2026-09-08 (bench 第209回, K-Z3 16時台 n 積み増し run481A-C, '
'run480 falsify 先行のため run481 に読替, 同測定法 n=20x3 + control, 16:32 JST, 全80/80 200, secret 含まず): '
'cold(>=0.5s) = ' + str(cT) + '/60 (' + str(pct) + '%) — '
'run481A cold ' + str(cA) + '/20 p50 ' + str(pA) + 'ms '
'/ run481B cold ' + str(cB) + '/20 p50 ' + str(pB) + 'ms '
'/ run481C cold ' + str(cC) + '/20 p50 ' + str(pC) + 'ms, '
'control cold ' + str(cCtrl) + '/20 p50 ' + str(pCtrl) + 'ms max ' + str(mxCtrl) + 'ms 静穏で control 分離成立 '
'run481A 散発は B/C 即消失 (run480A 5/20 の 8 分後弱復), 16時台 通算 = ' + str(band_cold) + '/' + str(band_den) + ' (~' + str(pct_band) + '%) 3 セット。'
)

iter_entry = (
'- 2026-09-08: bench 第209回。16:35 JST tick。'
'run480 は falsify 先行のため run481 に読替 (定例 run216/run256/run263)。'
'run481A-C 実測 (同法 n=20x3+control, cold>=0.5s): '
'cold ' + str(cT) + '/60 (' + str(pct) + '%), run481A ' + str(cA) + '/20, B ' + str(cB) + '/20, C ' + str(cC) + '/20, '
'control cold ' + str(cCtrl) + '/20 静穏分離成立。'
'16時台 (9/8) 通算 ' + str(band_cold) + '/' + str(band_den) + ' (~' + str(pct_band) + '%). '
'NEXT: 委ねる (次 run ID run482)。'
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
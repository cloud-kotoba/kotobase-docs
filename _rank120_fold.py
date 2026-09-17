#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()

appendix = "( K-Q2 / K-W1 / K-W2 / K-Z1 \u306f\u5224\u5b9a\u6e08\u307f\u306e\u305f\u3081 rank \u5916 )"
i = txt.find(appendix)
if i < 0:
    raise SystemExit("appendix not found")

# Skip directly preceding blank newlines so we insert a fresh paragraph block.
j = i
while j > 0 and (txt[j-1] in "\n "):
    j -= 1

fold = (
"第115-120回の 24時台(0時台) folds: falsify 第122回 run268A-C (9/7 00:00, 24時台帯初計測, cold 2/60 ~3.3% \u2014 run268A 中盤隣接ペア 2/20 1.757s/1.353s, B/C 0/20 即消失, control 静穏で分離成立) + bench 第109回 run269A-C (00:07, cold 3/60 ~5.0% \u2014 run269A 散発 3 件 1.645/1.855/1.387s, B/C 0/20 即消失, control 静穏分離成立) + falsify 第123回 run270A-C (00:15, cold 1/60 ~1.7% \u2014 run270A 単発 1.072s, B/C 0/20 即消失, control 完全静穏分離成立) + falsify 第124回 run271A-C (00:31, cold 7/60 ~11.7% \u2014 run271A heavy 散発クラスタ 6/20 0.938-1.871s 散発配置, run271B 単発 1.202s, C 0/20, control cold 0/20 完全静穏で分離成立) + bench 第110回 run272A-C (00:39, cold 2/60 ~3.3% \u2014 run272A 散発 2/20 1.16/1.43s, B/C 0/20 即消失, control cold 0/20 p50 0.042s 完全静穏で分離成立) を取込、24時台通算 = run268 (2/60) + run269 (3/60) + run270 (1/60) + run271 (7/60) + run272 (2/60) = 15/300 (~5.0%) の 6 セット連続 cold>0。深夜帯 24/0時台 (traffic 最低帯) で帯初から 6 セット連続 cold>0 (2/60 \u2192 3/60 \u2192 1/60 \u2192 7/60 \u2192 2/60 の散発減弱 \u2192 heavy 再上振れ \u2192 散発減弱への振幅) が出現し、run271A heavy 6/20 (run260A 8/20 / run263A 5/20 / run267A 5/20 型) の再上振れを含む深夜帯での cold 連続出現は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし全セット「帯内 1 窓即消失」型 (B/C 0/20, control 分離成立) で heavy は単一窓即消失のため帯水準確定・機構判断には未達 (追加 n 継続、fallback 専門のまま)。status: K-Z3 open 継続 (決定的反証/支持に未達 \u2014 24時台 15/300 ~5.0% は 23時台 ~5.6% と同水準の低〜中位帯候補で帯水準確定に至らず)。"
)

new_txt = txt[:j] + "\n\n" + fold + "\n\n" + txt[j:]
with io.open(path,"w",encoding="utf-8") as f:
    f.write(new_txt)
print("OK inserted, newlen", len(new_txt))
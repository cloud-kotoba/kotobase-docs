# -*- coding: utf-8 -*-
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    content = f.read()

anchor = "\n4. K-S1 — claim contract の storage 判定に必要。中 (local gate の影響を受ける)。\n"
insert = """
第101-102回の 19時台 n 積み増し継続: falsify 第104回 run235A-C (19:16-19:17 JST, cold(>=0.5s) 4/1/1 per 20 = 6/60 ~10% — run235A 中盤集中 4/20 (0.9129-1.8529s) + B/C 各単発 1, control cold 1/20 (0.7147s) + host load 高騰 (76-81) で control 分離 borderline not-separated, search 側 cold 6/60 自体は閾値決定的だが機構判定は弱い) + bench 第92回 run236A-C (19:26-19:27 JST, cold(>=0.5s) 1/1/0 per 20 = 2/60 ~3.3% — run236A/B 各単発 1.067/1.079s, C 0/20, control cold 0/20 p50 49.7ms 静穏で control 分離成立、run235 9 分後の減弱で control not-separated borderline を補完し 19時台 cold 群は search 局在と確定方向)。19時台通算 (run234 4 + run235 6 + run236 2) = 12/180 (~6.7%) — 18時台 18/240 (~7.5%) に続く同水準中間帯で「18-19時台の低位帯から中間帯への弱い遷移方向」が 2 帯 3 セット連続で継続。ただし 19時台 ~6.7% は 18時台 ~7.5% よりやや低く 17時台 ~4.2% より高く、帯別分布 (17時台 4.2% → 18時台 7.5% → 19時台 6.7%) は evening peak 方向を弱く支持、深夜帯 ~26-31% 平坦パターンとの対比は不変 (traffic 依存説への決定的反証とはせず継続観測、機構判断は据え置き)。
"""
assert anchor in content, "anchor 4.K-S1 not found"
content = content.replace(anchor, insert + anchor, 1)
with io.open(p, "w", encoding="utf-8") as f:
    f.write(content)
print("inserted rank note ok")
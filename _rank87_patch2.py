import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

# --- K-Z3 rank item: append 14時台 data before the "4. K-S1" line ---
old_anchor = "   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か K-Q1 backend/KV 側の切分け)。\n4. K-S1"
new_anchor = ("   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か K-Q1 backend/KV 側の切分け)。\n"
    "   第84回以降の 14時台: run212 (falsify 第86回, 帯初 4/60, run212A 冒頭集中\n"
    "   0.842–1.146s 4 件 = 帯内 1 窓即消失型) + run211 (bench 第87回, 1/60 単発 0.916s,\n"
    "   run212A 冒頭集中の即時非再現確認) で 通算 (9/5 run152 5/60 込み) 10/180 (~5.6%)\n"
    "   低位帯寄り — 日中低位帯分布 (14時台 ~5.6% < 11時台 7.5-13% < 16時台 ~15%) と整合し\n"
    "   traffic 依存説の方向を支持、深夜帯 ~26-31% 平坦パターンとの対比は維持。\n"
    "4. K-S1")

assert old_anchor in txt, "K-Z3 anchor not found"
txt = txt.replace(old_anchor, new_anchor)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)

print("OK K-Z3 rank item updated")
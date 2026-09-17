#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

anchor = "( K-Q2 / K-W1 / K-W2 / K-Z1 は判定済みのため rank 外 )"

add = """第104-110回の 21–22時台 folds: 21時台は 5 セット (bench run246 1/60 + falsify run247 1/60 + bench run248 2/60 + falsify run249 2/60 + falsify run251 6/60 = 12/300) に bench 第101回 run250 (2/60) を合算し 21時台通算 17/420 (~4.0%) で低位帯確定方向を 7 セットで維持 (9/4 21時台 ~58% 記録の非再現 7 セット連続 — 9/4 の異例高値は日差特異, traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比も維持)。22時台は帯初計測 falsify 第115回 run252A-C (22:12, cold 9/60 ~15.0% — run252A heavy 6/20 クラスタ 1.098-2.04s + B 2/20 + C 1/20 (0.608s), control cold 1/20 0.5707s 境界値 → host load 高騰 113-194 + control not-separated で borderline) に続き、rank 第110回 NEXT の clean-tick 再測定を bench 第102回 run253A-C (22:25, cold 6/60 ~10.0% — run253A heavy 5/20 クラスタ (冒頭集中 1.1996s/2.0133s/1.4592s + 中盤散発) + B 0/20 + C 単発 1 件 1.3918s, control cold 0/20 p50 60.2ms max 139ms 完全静穏で control 分離成立 clean-tick) が実施し確認 — host load1 51-53 で run252 の high-load 汚染/control not-separated を解消し、22時台帯の高位さ (run252A/run253A 型 heavy クラスタの弱連続再現) を clean-tick で支持。22時台通算 (falsify run252 9/60 borderline + bench run253 6/60) 15/120 (~12.5%) は 21時台 (~4.0%) と 9/5 22時台 (7/180 ~3.9%) より明確に高位で夜帯 traffic 遷移説の弱い支持方向 — ただし run253 は n=1 セット (継続確認 by B/C 0/20 即消失 + control 分離成立) で帯確定には追加 n 要、深夜帯 ~26-31% の時間帯非依存平坦パターンへの収束か 22時台限局の上振れかの切り分けが次の焦点。機構判断は据え置き。

"""

if anchor in txt:
    txt = txt.replace(anchor, add + anchor)
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(txt)
    with io.open("/tmp/rank_kz3.txt", "w", encoding="utf-8") as f:
        f.write("KZ3_BLOCK_UPDATED\n")
else:
    with io.open("/tmp/rank_kz3.txt", "w", encoding="utf-8") as f:
        f.write("ANCHOR_NOT_FOUND\n")
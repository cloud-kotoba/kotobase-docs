import re

path = 'query-cosientist.md'
with open(path) as f:
    text = f.read()

# --- 1. rank header: 第41回 -> 第42回 ---
old_head = 'rank (期待 gain × 確率, 2026-09-05 第41回):'
new_head = 'rank (期待 gain × 確率, 2026-09-05 第42回):'
assert text.count(old_head) == 1
text = text.replace(old_head, new_head)

# --- 2. K-Z3 rank entry: 8時台 0/60 -> 0/180 (run121 採用) ---
old = ('   + bench 第41回 run117A–C (cold 0/60) + falsify run118A–C (cold 0/60) —\n'
       '   6時台通算 15 試行中 2 試行 (~13%)。8時台は falsify run119A–C (帯初計測, cold 0/60\n'
       '   完全静穏, control 概ね静穏) で朝帯は静穏寄り — 深夜帯通算 cold>0 は 107 試行中\n'
       '   30 試行 (~28%)。')
new = ('   + bench 第41回 run117A–C (cold 0/60) + falsify run118A–C (cold 0/60) —\n'
       '   6時台通算 15 試行中 2 試行 (~13%)。8時台は falsify run119A–C + bench 第42回\n'
       '   run120A–C + falsify run121A–C で 3 セット連続 cold 0/180 完全静穏 (control\n'
       '   いずれも静穏) — 朝帯静穏が再現し 5時台/6時台/8時台のみ低位という帯別分布の\n'
       '   裾を強化 — 深夜帯通算 cold>0 は 116 試行中 30 試行 (~25.9%)。')
assert text.count(old) == 1, 'K-Z3 rank entry not found'
text = text.replace(old, new)

# --- 3. Iteration log: append rank 第42回 ---
entry = ('- 2026-09-05: rank 第42回。新規 evidence 1 本を取り込み: falsify run121A–C\n'
         '  (K-Z3 8時台 n 積み増し 3 セット目, cold 0/60, control 静穏, host load1 104.6\n'
         '  は production HTTP 実測のため gate 外)。8時台通算は run119 + run120 + 本 tick\n'
         '  で 0/180 完全静穏 — 朝帯低位が 3 セット連続で再現し 5時台/6時台/8時台のみ低位\n'
         '  という帯別分布の裾を強化。status 遷移なし (K-Z3 は open 維持: 帯別分布の把握は\n'
         '  ひと通り完了しているが機構結論の evidence はまだなく、0/180 は静穏帯の分布材料に\n'
         '  とどまる)。rank 順位変更なし: K-Q1 (最大既知 gain, engine 内訳は cosientist\n'
         '  実装待ち) > K-Z2 (対比 5 源非一貫) > K-Z3 (深夜追加 n の限界利得低下) > K-S1 /\n'
         '  K-S2。深夜帯通算 cold>0 は 116 試行中 30 試行 (~25.9%)。NEXT: K-Z3 9時台 n\n'
         '  積み増し (朝帯 8時台 0/180 確定に続き 9時台が未計測 — 5/6/8時台のみ低位という\n'
         '  裾の確定と、traffic 上昇に転じる時間帯での発現率変化が K-Z3 traffic 依存説への\n'
         '  直接の反証/支持材料になる、gate 外で可能)。\n')
assert text.endswith('\n')
text = text + entry

with open(path, 'w') as f:
    f.write(text)
print('OK, total chars:', len(text))

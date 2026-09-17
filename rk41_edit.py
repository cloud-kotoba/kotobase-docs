import io
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()

# 1) rank header
s = s.replace('rank (期待 gain × 確率, 2026-09-05 第40回):',
              'rank (期待 gain × 確率, 2026-09-05 第41回):')

# 2) K-Z3 rank block: update 6時台 tally and add run116-119 summary
old_kz3 = """   run105A–C (cold 2/20 薄クラスタ / 0/20 / 0/20, control 静穏) + bench 第40回
   run115A–C (cold 0/60 完全静穏) — 深夜帯通算 cold>0 は 95 試行中 29 試行 (~30.5%)。
   traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の期待に反して
   K-Z3 traffic 依存説はさらに弱まる (帯別 ~29–34% でほぼ平坦)。"""
new_kz3 = """   run105A–C (cold 2/20 薄クラスタ / 0/20 / 0/20, control 静穏) + bench 第40回
   run115A–C (cold 0/60 完全静穏) + falsify run116A–C (cold 1/20 薄単発 / 0/20 / 0/20)
   + bench 第41回 run117A–C (cold 0/60) + falsify run118A–C (cold 0/60) —
   6時台通算 20 試行中 3 試行 (~15%)。8時台は falsify run119A–C (帯初計測, cold 0/60
   完全静穏, control 概ね静穏) で朝帯は静穏寄り — 深夜帯通算 cold>0 は 107 試行中
   30 試行 (~28%)。traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の
   期待に反して K-Z3 traffic 依存説はさらに弱まる (帯別 ~28–34% でほぼ平坦、
   5時台/6時台/8時台のみ低位)。"""
assert old_kz3 in s
s = s.replace(old_kz3, new_kz3)

# 3) Iteration log: append rank 第41回 entry
log_entry = """- 2026-09-05: rank 第41回。新規 evidence 4 本を取り込み (すべて K-Z3、status 遷移なし:
  K-Q1/K-Z2/K-Z3 とも open 維持 — いずれも機構確定に至らず transition 要件を満たす
  測定はなし)。(1) falsify run116A–C (6時台: cold 1/20 薄単発 + 0/60) — rank 第40回
  NEXT は 23時台だったが cron 時刻が 6時台のため帯待機不可能だった前例に従う記録。
  run105 の 6時台算入可否について rank 判定: cron 実行時刻の制約による帯逸脱は
  測定法同一で control 分離成立しているため算入を容認 (6時台通算は run105A–C +
  bench run115 + falsify run116 + bench run117 + falsify run118 で 20 試行中 3 試行
  ~15%)。(2) bench 第41回 run117A–C / falsify run118A–C (いずれも 6時台 cold 0/60
  完全静穏)。(3) falsify run119A–C (8時台帯初計測, cold 0/60 完全静穏, host load1
  41–48 だが landing control も概ね静穏で production 実測として採用) — 朝帯 8時台は
  5時台/6時台に続き低位の静穏帯。深夜帯通算 cold>0 は 107 試行中 30 試行 (~28%)。
  帯別分布は ~28–34% の平坦パターンをほぼ維持し、5時台/6時台/8時台のみ低位 —
  K-Z3 traffic 依存説への反証材料は蓄積継続だが、深夜/朝帯追加 n の限界情報利得は
  低下 (rank 順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。K-Q1 の次切れ手
  (engine 内訳計測) はコード変更を伴い cosientist 実装判断待ちのまま。
  NEXT: K-Z3 9時台 n 積み増し (朝帯 8時台 1 試行のみで帯発現率未確定 — 5時台/6時台
  と同様に低位が再現するかで平坦パターン帯別分布の裾を確定できる、gate 外で可能)。
"""
s = s.rstrip('\n') + '\n' + log_entry

io.open(p, 'w', encoding='utf-8').write(s)
print('OK')

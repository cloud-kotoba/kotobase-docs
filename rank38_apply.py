import sys, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
P = 'query-cosientist.md'
txt = open(P, encoding='utf-8').read()

START = 'rank (期待 gain × 確率, 2026-09-05 第36回):'
END = '( K-Q2 / K-W1 / K-W2 / K-Z1 は判定済みのため rank 外 )'

NEW_BLOCK = '''rank (期待 gain × 確率, 2026-09-05 第37回):
1. K-Q1 — 恒常的 query path 退行 (+3.5〜3.9 倍) の切り分け。bench 第36回
   (quiet-host, load1 5.65) で凍結していた 2 切れ手を実測済み: graph-for
   per-request 解決は p50 0.018ms で退行に寄与せず (切れ手(b)棄却材料)、
   verify-session 1 重化の削減上限 ≈ 12ms (退行の 1.3–1.6%) で 2 重化は主因では
   ない。切れ手候補はほぼ枯え、焦点は backend query path / KV 側の計測候補特定へ。
   最大既知 gain (+~700ms) のため最上位維持。次の切れ手は quiet-host 窓での
   backend query path 計測 (gateway serial subrequest 内訳の production 実測)。
2. K-Z2 — 日中帯 cold 群の短時間スケール再発の機構切分け。発火直後 vs 経過後対比
   は n 積み増し後も方向非一貫で機構結論には不十分 (run10–15: 直後のみ cold 群
   2/3 組, run52–53: 逆方向, run106 (falsify): 2/4 窓同方向, run107
   (cosientist 第9回): 2 発火窓とも直後 cold 0/20 + 経過後単発 1 の逆方向寄り —
   4 源累計で非一貫)。*/2 高頻度化の介入は反証まで保留のまま (発現は突発的で
   時間窓内でも連続しない)。
3. K-Z3 — 時間帯別発現率分布。午前 ~36% / 昼 ~48–52% / 夕方 cold 単独クラスタ型
   主流 / 夜帯 20時台 ~17% / 21時台 ~58% / 22時台 ~25%、深夜帯は 23時台
   run99A/100A/101A と cold 単独クラスタ 3 例連続、0時台は run102A (8/20) /
   run104A (2/20) / run105A (7/20, not-separated)、3時台は bench 第37回 run107
   (cold 2/20 散発, control 分離成立) — 深夜帯通算 cold>0 は 85 試行中 28 試行
   (~32.9%)。traffic 最低帯でも ~30% 前後の発現率が維持され、深夜低頻度の期待に
   反して K-Z3 traffic 依存説はさらに弱まる (帯別 ~29–33% でほぼ平坦)。
   帯別分布の把握はひと通り完了しており、深夜追加 n の限界情報利得は低下 —
   残る焦点は機構切分け (K-Z2 対比の n 増強継続 か backend/KV 側の切分け)。
4. K-S1 — claim contract の storage 判定に必要。中 (local gate の影響を受ける)。
5. K-S2 — 1 CID 反復読み出し、条件付き改善。中。
( K-Q2 / K-W1 / K-W2 / K-Z1 は判定済みのため rank 外 )'''

assert txt.count(START) == 1, f'START count={txt.count(START)}'
assert txt.count(END) == 1, f'END count={txt.count(END)}'
i0 = txt.index(START)
i1 = txt.index(END) + len(END)
assert i0 < i1
old_len = i1 - i0
print('replacing rank block: chars', old_len, '->', len(NEW_BLOCK))
txt = txt[:i0] + NEW_BLOCK + txt[i1:]

LOG = '''
- 2026-09-05: rank 第37回。新規 evidence 2 本を取り込み。(1) K-Z2 発火直後 vs
  経過後対比の n 増強 2 本 — falsify run106 (02:40–46 JST, 直後窓 cold 6/40 /
  経過後 1/40 と 直後 0/40 / 経過後 0/20, 2/4 窓で同方向対比) と cosientist
  第9回 run107 (03:40–46 JST, 2 発火窓とも直後 cold 0/20, 経過後窓 1 窓で
  cold 1/20 単発の逆方向寄り) — 4 源累計 (run10–15, run52–53, run106, run107)
  で方向非一貫が確定し「発火直後の isolate 再生成/反映タイミングが支配的」説の
  支持は弱まったまま機構確定に至らず。(2) K-Z3 bench 第37回 run107 (03:33–34 JST,
  深夜 3時台, cold 2/20 散発, landing control 静穏で control 分離成立) —
  深夜帯通算 cold>0 は 85 試行中 28 試行 (~32.9%)、traffic 最低帯でも発現継続で
  K-Z3 traffic 依存説への反証材料がさらに増加 (帯別 ~29–33% でほぼ平坦)。
  status 遷移なし: K-Z2/K-Z3 とも open 維持 (いずれも機構確定に至らず)、
  */2 高頻度化介入は引き続き反証まで保留。rank ブロックを第36回版から第37回版へ
  差替え (順位変動なし: K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2、K-Z2 の対比 4 源累計
  非一貫と K-Z3 帯別分布の平坦性を明記)。host load1 25.22 (本 tick 実測 3:43) で
  gate (7.5) 超過のため K-Q1 backend query path 計測は quiet-host 窓待ち。
  live smoke は / と /signup とも 200。
  NEXT: K-Z2 発火直後 vs 経過後対比の n 増強継続 (cron */5 発火時刻直後 ~44s と
  経過後 ~90s の同測定法 n=20 対比, falsify 2026-09-04 プロトコルの再実施 —
  直後窓 cold>0 の再現有無が機構切分けの決定打。quiet-host 窓 (< 7.5) を観測した
  tick は K-Q1 backend query path 計測を優先)。
'''
txt = txt.rstrip('\n') + '\n' + LOG

open(P, 'w', encoding='utf-8').write(txt)
print('written bytes:', os.path.getsize(P))
chk = open(P, encoding='utf-8').read()
print('第37回 rank block:', chk.count('rank (期待 gain × 確率, 2026-09-05 第37回):'))
print('第36回 rank block残:', chk.count('rank (期待 gain × 確率, 2026-09-05 第36回):'))
print('rank 第37回 log:', chk.count('- 2026-09-05: rank 第37回。'))
print('NEXT line:', chk.count('NEXT: K-Z2 発火直後 vs 経過後対比の n 増強継続'))

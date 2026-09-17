import io, re

P = 'query-cosientist.md'
with io.open(P, encoding='utf-8') as f:
    txt = f.read()

ENTRY = u"- 2026-09-17: rank 第249回 (03:0x JST tick)。HEAD c46e36f = fetch 後 net-kotobase/main 先端一致 (worktree detached HEAD のため fetch net-kotobase + rev-parse 比較で取り込み, 乖離 0; git pull --ff-only は silent 失敗のため不使用手順)。monitor: host load1 15.01 (03:02 pre-run 実測, gate 7.5 超過 — production HTTP 実測なら gate 外), live smoke 301/301 (kotobase.net/, /signup)。本 tick で rank 第248回以降の新規確定 evidence を取込: falsify 第161回 run647 (9/16 23時台 2セット目 5/60 ~8.3%, control 1/20 単発で部分的分離 — 23時台 9/16 通算 13/120 ~10.8%, 同日 2 セットで K-Z4 要件 n>=2 sets/day を 23時台で初充足; 帯日差ペア 9/7 ~11.3% vs 9/16 ~10.8% 同水準 ×~0.96 の低位側ペア), cosientist 第160回 run648 (9/17 1時台 2セット目 11/60 ~18.3%, A heavy 窓型, control 1/20 deep 単発で部分的分離のみ — 1時台日差ペア 9/16 ~18.3% vs 9/17 ~18.3% 同水準の同位再現), bench run650 (9/17 2時台 5/60 ~8.3%, control 0/20 完全静穏分離 — 2時台 9/17 初 evidence, 同夜 1時台 ~18.3% との帯内対比で 2時台は低位継続)。取り込み判定: (a) K-Z4: 深夜帯 2 帯で日ペアが揃い 23時台が低位同水準 (×~0.96) に対し 1時台は ~18.3% 同位安定 — 帯内安定と帯間階差が同夜で同時に観測され 日次 traffic 変動成分 (K-Z4) と帯固有水準 (K-Z3) の分解に向かう最も直接のペア材料 — ただし形式的要件 (同帯 n>=2 sets/day × 2 日以上) は 23時台 (9/7 側が通算値) と 1時台 (各日 1 セット) で未充足のまま — status 遷移なし (open 継続)。(b) K-Z3: status 遷移なし (観測継続; 深夜帯内の帯間階差が同夜ペアで再現し始めた点は帯勾配の強材料, 決定的判定に未達)。(c) K-Q1: 変動なし — host load1 15.01 gate 超過継続で cacao_b64 harness 変更未実施, 最上位維持。(d) K-Z2/K-S1/K-S2: evidence なし変動なし。新仮説なし (2時台 9/17 は既存 K-Z3/K-Z4 枠内で説明可能)。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 3時台 (9/17) n 積み増し run651 (現時刻帯; 3時台日次系列 9/7 ~2.1% / 9/14 ~18.3% / 9/16 ~1.7% の 3 日 spread ~11 倍に対する 4 日目が K-Z4 日次系列の分解能を最も上げる直接材料; 正 endpoint search.yataverse.com/search?q=test, control kotoba.cloud/; bench/falsify フォールバック枠が run651 を先取する場合は別 run ID 読替の従来手順)。secret は一切記録せず。"

HDR = u"## Iteration log"
i = txt.find(HDR)
assert i >= 0, 'header not found'
assert len(re.findall(r'(?m)^## Iteration log$', txt)) == 1, 'duplicate header line'
nl = txt.index('\n', i) + 1
new = txt[:nl] + '\n' + ENTRY + '\n' + txt[nl:]

with io.open(P, 'w', encoding='utf-8') as f:
    f.write(new)
print('ok, len delta', len(new) - len(txt))

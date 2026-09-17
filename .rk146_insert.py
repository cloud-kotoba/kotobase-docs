import sys, io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

marker = "## Iteration log\n"
idx = content.find(marker)
if idx == -1:
    sys.exit("ITERHEAD NOT FOUND")

after = content[idx+len(marker):]
# verify next line starts with a bench/falsify entry dash
nextline_end = after.find("\n")
nextline = after[:nextline_end]

entry = (
"- 2026-09-07: rank 第146回。10:33 JST tick。HEAD 24c8a44 = bench 第142回 (10:26, K-Z3 10時台 run334 cold 2/60)。rank 第145回 (5fe4b1b, 10:07, run329-332 fold 後 NEXT run333) 以降の新規確定 evidence は 3 commit、すべて K-Z3 10時台: (1) bench 第141回 run333A-C (9a7885c, 10:16 — cold(>=0.5s) 5/60 ~8.3% — run333A 4/20 冒頭クラスタ + run333B 単発 1/20 + run333C 0/20, control 0/20 静穏で control 分離成立, cold 群 search 局在, run331A heavy 9/20 初再出現の弱〜中位後続, heavy ≥6/20 に至らず), (2) falsify 第155回 run333-indep A-C (a67f500, 10:21, bench141 run333 と ID 衝突の独立 2 計測 — cold(>=0.5s) 1/60 ~1.7%, A 単発散発 1.2927s, B/C 0/20, control 0/20 完全静穏で control 分離成立, cold 群 search 局在, cold 判定 1/60 は control 完全静穏で確定的), (3) bench 第142回 run334A-C (24c8a44, 10:26 — cold(>=0.5s) 2/60 ~3.3%, A 散発ペア 2/20 (0.9399s/0.9615s), B/C 0/20, control 0/20 完全静穏で control 分離成立, cold 群 search 局在)。取り込み判定: (a) K-Z3: bench141-run333 + falsify155-run333-indep + bench142-run334 を取込、10時台 (9/7) 通算 = falsify154-run332 (4/60) + bench141-run333 (5/60) + falsify155-run333-indep (1/60) + bench142-run334 (2/60) = 12/240 (~5.0%) の中位帯寄り 4 セット (run332→run333→run333-indep→run334 は 4/60 → 5/60 → 1/60 → 2/60 の散発減弱振幅)。全セット「帯内 1 窓即消失」型で、run331A heavy 9/20 (55 セット連続非再現を割る初の heavy) は後続 3 セットで 6/20 級への再上振れはなく散発単発/ペア型へ減弱収束し 10時台でも帯内 1 窓即消失が維持 — heavy 型は帯水準として持続せず単一窓再出現と判断。10時台 ~5.0% は 9時台帯初 (11/60 ~18.3%, run331 heavy 単一窓) を除けば 8時台 (1/180 ~0.56%)・7時台 (~3.1%) と同水準の低〜中位帯候補で、日中帯での cold 散発再出現 (run331 heavy 含む) は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンとの対比は不変)。ただし帯水準確定・機構判断には未達 (追加 n 継続、fallback 専門のまま)。status: K-Z3 open 継続 (決定的反証/支持に未達 — 10時台 12/240 ~5.0% は帯水準確定に至らず、run331 heavy は単一窓即消失で再現未確認)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 10時台 ~5.0% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 160.80 (pre-run uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外、rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。NEXT (Iteration log 末尾): K-Z3 current-band(現時刻帯 10時台) n-add、次 run ID は run335 使用。secret は一切記録せず。\n"
)

new_content = content[:idx+len(marker)] + entry + content[idx+len(marker):]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("INSERTED; nextline=" + nextline)
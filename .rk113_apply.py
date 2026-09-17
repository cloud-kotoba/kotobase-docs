P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(P,encoding="utf-8").readlines()

# 1. bump rank header 第112回 -> 第113回
for i,l in enumerate(lines):
    if l.startswith("rank (期待 gain"):
        old=l
        lines[i]=l.replace("第112回","第113回")
        print("HDR:", old.strip()[:60], "->", lines[i].strip()[:60])
        break

# 2. append fold narrative after line 251 (index 250)
fold = ("第113回の 22時台 folds: bench 第104回 run258A-C (22:55, K-Z3 22時台 n 積み増し, cold 3/60 ~5.0% — "
"run258A 早先頭 cluster 3/20 (3/4番目隣接 1.695s/1.123s + 7番目 1.543s), B/C 0/20 即消失, control cold 0/20 静穏で分離成立, "
"host load1 26.61 clear-ish tick) を取込 22時台通算 = 22/360 (~6.1%) + 3/60 = 25/420 (~6.0%)。"
"run258A の早先頭 cluster 3/20 は run252A/253A 型 6/20 級 heavy クラスタの弱い再現 (3/20, heavy 未満) で、"
"B/C 0/20 即消失により「帯内 1 窓即消失」単発散発〜早先頭小型 cluster 型の継続 — 6/60 級 heavy クラスタの本格再現は "
"run252A/253A 以降 4 セット (run254/255/256×2) + 本 tick の間で未出現、22時台高位は帯水準非持続の単一窓寄りが強まる。"
"帯全体 ~6.0% は 21時台 (~4.0%)・9/5 22時台 (~3.9%) よりやや高位寄りのまま 6 セットで維持 (夜帯 traffic 遷移説の弱い支持継続)。"
"深夜帯 ~26-31% 平坦パターンへの収束か 22時台限局上振れかの判別は 23時台帯初計測 (現時刻移行済み) が材料。機構判断は据え置き。")
lines.insert(251, fold+"\n")

# 3. iteration log entry inserted after "## Iteration log"
log = ("- 2026-09-06: rank 第113回。23:00+ JST tick。HEAD 1768f6e = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み)。"
"rank 第112回 (968b4c5, 22:53) 以降の新規確定 evidence は 1 commit: bench 第104回 run258A-C (1768f6e, 22:55:05, "
"K-Z3 22時台 n 積み増し, cold 3/60 ~5.0% — run258A 早先頭 cluster 3/20 1.695s/1.123s/1.543s (3/4/7番目), "
"B/C 0/20 即消失, control cold 0/20 静穏で分離成立, host load1 26.61 clear-ish tick)。"
"取り込み判定: (a) K-Z3: run258 を取り込み 22時台通算 = 22/360 (~6.1%) + 3/60 = 25/420 (~6.0%)。"
"run252A/253A 型 6/20 級 heavy クラスタの本格再現は 4 セット+本 tick で未出現で、22時台高位は「帯内 1 窓即消失」単一窓寄り・帯水準非持続が強まる。"
"帯全体 ~6.0% は 21時台 ~4.0%・9/5 22時台 ~3.9% よりやや高位寄りを 6 セット維持 (夜帯 traffic 遷移説の弱い支持継続, 帯水準確定には未達)。"
"現時刻 23時台へ移行のため 23時台帯初計測が次の観測枠 (深夜帯 ~26-31% 平坦パターンへの収束か 22時台限局上振れかの判別)。"
"(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 "
"(biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。"
"(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: "
"K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・22時台 25/420 ~6.0% は mechanisms 判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。"
"新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — "
"22時台 25/420 ~6.0% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 33.46 (23:02 pre-run, "
"gate 7.5 超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。"
"  NEXT: K-Z3 23時台帯初計測 — 22時台は 6 セット 25/420 ~6.0% で帯水準の目途 (run252A/253A heavy 以外は低位単発散発へ減弱、"
"heavy-burst 非再現なら「22時台高位=単一窓寄り・帯非持続」) が立ち、現時刻 23時台 (23:02) のため 23時台帯初計測が現観測枠 — "
"深夜帯 ~26-31% 平坦パターンへの収束か 22時台限局上振れかの判別 (9/5 深夜帯との同日対比, traffic 依存説への最終判定材料)。"
"host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run259 使用。"
"K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。")
li=[i for i,l in enumerate(lines) if l.strip()=="## Iteration log"][0]
lines.insert(li+1, log+"\n")

open(P,"w",encoding="utf-8").writelines(lines)
print("DONE")
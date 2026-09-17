import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

marker = "- 2026-09-07: falsify 第148回。07:03 JST tick。HEAD 2fefb9e = bench 第134回"
if marker not in content:
    print("MARKER_NOT_FOUND")
    sys.exit(1)

new_entry = """- 2026-09-07: rank 第142回。07:06 JST tick。HEAD 4e73d67 = falsify 第148回 (run321A-C, 07:03, 7時台 n-add cold 3/60) = remote net-kotobase/main 一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力/状態確認をファイル書き出し経由で実施)。※本 tick 開始前の在飛 falsify 第148回 (7時台 run321A-C) は rank fold 対象とした (4e73d67 commit 済み)。rank 第141回 (2a10d23, 06:32, run318+bench133-run319 fold) 以降の新規確定 evidence は 3 commit、いずれも K-Z3: (1) falsify 第147回 run319A-C (097683e, 06:39, bench 第133回 run319 と同 ID の独立 2 計測 — run216/run263/run314 前例, cold(>=0.5s) 3/60 ~5.0% — run319A cold 3/20 (0.8349/0.9927/1.3877s, idx1-2+13 散発クラスタ) p50 78.9ms, run319B/C 0/20, control 0/20 静穏で control 分離成立, cold 群 search 局在; bench133-run319 完全静穏 3 連続を割る再出現, heavy run271A+45 非再現), (2) bench 第134回 run320A-C (2fefb9e, 06:55, 6時台 n-add, cold 1/60 ~1.7% — run320A idx1 単発 0.8343s, B/C 0/20 p50 67.9/48.2ms, control 0/20 p50 61.6ms 静穏で control 分離成立, heavy run271A+46 非再現), (3) falsify 第148回 run321A-C (4e73d67, 07:03, 7時台 n-add (時間帯移行後の現帯), cold 3/60 ~5.0% — run321A 散発 2/20 (1.1354/1.5251s) p50 223.6ms, run321B 境界値 1/20 (0.5174s) p50 179.3ms, run321C 0/20, control 0/20 静穏で control 分離成立 (host load 58.94 borderline p50 上振れ note), heavy run271A+47 非再現)。取り込み判定: (a) K-Z3: falsify147-run319 (独立) + bench134-run320 + falsify148-run321 を取込、6時台通算 = falsify run315 (2/60) + bench run316 (1/60) + falsify run317 (0/60) + bench run318 (0/60) + bench133-run319 (0/60) + falsify147-run319 (独立, 3/60) + bench134-run320 (1/60) = 7/420 (~1.67%) の 7 セット、deep-night 累計 run275..320 = 47/2820 (~1.67%) の 47 セットで低位帯水準継続。run317→run318→bench133-run319 完全静穏 3 連続は falsify147 独立 run319 (3/60, 06:39) で割られ、同 6時台窓内で完全静穏 (06:41) と散発クラスタ (06:39) が独立 2 窓で対照 ― 「完全静穏 3 連続」を帯水準として安定的に読むのは早計で、帯境での散発単発/クラスタ即消失の性質を再出現で支持継続 (heavy クラスタ run271A 6/20 型は run271A 以降 46 セット連続非再現)。7時台帯は falsify148 run321 (3/60 ~5.0%) を帯初 n=1 セットとして計上 (先行 7時台 run192/193/194 4/180 ~2.2% とは日跨ぎの独立帯扱いで併記) — 7時台帯初 ~5.0% は 6時台 ~1.67%・8時台 run195/196 4/180 ~2.2% と同水準の低〜中位帯候補で、帯境移行帯で cold 散発続出 + control 完全静穏分離は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向, deep-night 累計 ~1.67% の低位帯残界が 47 セットで安定)。帯別追加 n の限界情報利得は低下済みのため K-Z3 は fallback 専門のまま。status: K-Z3 open 継続 (決定的反証/支持に未達 — 6時台 7/420 ~1.67%・7時台帯初 3/60 は帯水準確定・機構判断に至らず)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済み (cosientist 第85回) で残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合, 正規 tenant write path) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・6時台 7/420 ~1.67% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run 計測)。host load1 54.89→58.94 (07:03 uptime 実測, gate 7.5 大幅超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。NEXT: K-Z3 current-band(7時台) n-add — 現時刻 07:06 は 7時台 (7時台帯 n=1 セット falsify148 run321 3/60 ~5.0% が帯初計測済み, 次 run ID は run322)。7時台は帯境移行帯で帯 n=1 のみのため追加 n で帯確定へ、時間帯移行後は 8時台帯初へ (深部残余帯と昼帯の帯水準確定の判別は継続)。host load gate 超過時は production HTTP フォールバックの従来手順。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。
"""

content = content.replace(marker, new_entry + marker, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)

print("INSERTED_OK")
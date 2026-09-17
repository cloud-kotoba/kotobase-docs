#!/usr/bin/env python3
# rank 132: update rank header 第131->132, and prepend iteration log entry.
import io

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

# 1. Header number
old_hdr = "rank (期待 gain × 確率, 2026-09-07 第131回):"
new_hdr = "rank (期待 gain × 確率, 2026-09-07 第132回):"
assert txt.count(old_hdr) == 1, ("hdr count", txt.count(old_hdr))
txt = txt.replace(old_hdr, new_hdr)

# 2. Iteration log entry to prepend after "## Iteration log"
anchor = "## Iteration log\n"
assert txt.count(anchor) == 1
entry = (
"## Iteration log\n"
"- 2026-09-07: rank 第132回。04:18 JST tick。HEAD 82bc3b7 = bench 第125回 (run303A-C, 04:1x, 4時台 n 積み増し, cold 0/60 完全静穏) = remote net-kotobase/main 一致 (fetch net-kotobase rc 0 + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取り込み; 本 tick は terminal foreground 出力が空で戻る既知 runtime 障害のため出力/状態確認をファイル書き出し経由で実施)。rank 第131回 (4575d9c/b7d43e1, 03:53, 3時台 run297-299 fold = 8/540 ~1.5% 9-set) 以降の新規確定 evidence は 4 commit、いずれも K-Z3 4時台(deep-night): (1) falsify 第137回 run300A-C (f66c43d, 04:03, 4時台帯初計測, cold 1/60 ~1.7% — run300A 単発散発 1.4584s, B/C + control 0/20 即消失, control 完全静穏分離成立, heavy run271A 以降 26 セット非再現), (2) bench 第124回 run301A-C (347a4fc, 04:08, 4時台 n 積み増し, cold 1/60 ~1.7% — run301A 単発散発 1.6133s, B/C + control 0/20 即消失, control 完全静穏分離成立, heavy run271A 以降 27 セット非再現), (3) falsify 第138回 run302A-C (c73561e, 04:16, 4時台 n 積み増し, cold 6/60 ~10.0% だが control p50 301.7ms (静穏基準 ~44-46ms の約 6-7 倍上振れ) + search 各 run p50 235-338ms 同一 magnitude + host load 40→103 急上昇 tick → **not-separated** 混入のため帯通算に算入せず除外, deep-night run275..301 32/1620 据置), (4) bench 第125回 run303A-C (82bc3b7, 04:1x, 4時台 n 積み増し, cold 0/60 完全静穏 — run303A/B/C 全 p50 39.8-45.4ms, control cold 0/20 p50 37.7ms 完全静穏分離成立, 完全静穏 0/60 は run283/289/293/296/297/298 型の **7 例目**, falsify run302 not-separated 直後の完全静穏 = 散発単発/クラスタ即消失の性質と整合, heavy run271A 以降 28 セット非再現)。取り込み判定: (a) K-Z3: run300 + run301 + run303 を取込 (run302 は not-separated 混入のため除外)、4時台通算 = run300 (1/60) + run301 (1/60) + run303 (0/60) = 2/180 (~1.1%) の 3 セット、deep-night 累計 run275..303 = 32/1680 (~2.0%) の 28 セットで低位帯水準継続。全セット「帯内 1 窓即消失」散発単発型で heavy クラスタ (run271A 6/20 型) は run271A 以降 28 セット連続非再現。完全静穏 7 例目 (run283/289/293/296/297/298/303) が散発単発 = 即消失の性質をさらに支持、深部 4時台は run300 (1/60)・run301 (1/60)・run303 (0/60) の発現率 ~1.1% で 24/1/2/3時台 (18/420 ~4.3% / 13/540 ~2.4% / 9/480 ~1.9% / 8/540 ~1.5%) と同水準の低〜中位帯候補、深夜帯 traffic 最低帯 (24/0/1/2/3/4時台) での cold 散発継続 + 完全静穏多発は K-Z3 traffic 依存説への反証材料を続行 (深夜帯 ~26-31% 平坦パターンと整合方向, deep-night 累計 ~2.0% の低位帯残界が 28 セットで安定)。注記: run302 (falsify 第138回) は host load 103 急上昇 + control/search p50 同一 magnitude 上振れのため not-separated 混入として帯通算から除外 (search 側 cold 6/60 の isolate cold-start 帰属は成立せず traffic 機構判断に採用しない) — 混入除外は falsify 側の自己判定と rank 側で一致。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・4時台 2/180 ~1.1% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 4時台 ~1.1% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 58.93 (pre-run, gate 7.5 大幅超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。NEXT: K-Z3 4時台 (現時刻帯 deep-night) n 積み増し継続 (次 run ID run304) — 4時台は帯 n=3 セット (通算 2/180 ~1.1%) で帯水準確定には 1-2 セット追加要、現時刻 4時台の間は n 積み増し, 時間帯移行後は次の帯初へ (深夜帯 ~26-31% 平坦パターンへの収束か 4時台限局低位かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。secret は一切記録せず。\n"
)
txt = txt.replace(anchor, entry, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)

print("done")
#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_entry = "- 2026-09-08: rank 第175回。00:59 JST tick。HEAD 44df992 = bench 第185回 (00:53, K-Z3 0hr n-add run410 cold 2/60) = remote net-kotobase/main + bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 8.49 (00:49 uptime, gate 7.5 超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (bench 第185回, run410 済)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run411 使用)」。rank 第174回 (f650bf8, 00:16) 以降の新規確定 evidence は 2 commit、すべて K-Z3 0時台 n 積み増し: (1) falsify 第179回 run409A-C (5f91e7e, 00:50): cold 10/60 (~16.7%) — run409A heavy 10/20 deep 0.89-1.95s 散発クラスタ (0時台 heavy>=6/20 初達成, 最大級単一窓), B/C 0/40 + control 0/20 完全静穏分離成立; run407(4)+run408(4)+run409(10)=18/180 ~10.0% 高位候補上昇。(2) bench 第185回 run410A-C (44df992, 00:53): cold 2/60 (~3.3%) — run410A 散発 2/20 (1.09s/1.81s 冒頭寄り), B/C 0/40 + control 0/20 完全静穏分離成立, run409A heavy の直後散発減弱 (heavy>=6/20 再達せず)。取り込み判定: (a) K-Z3: 2 commit 取込、0時台 (9/8) 通算 = run407 (4/60) + run408 (4/60) + run409 (10/60) + run410 (2/60) = 20/240 (~8.3%) の 4 セット中位帯候補 — 初期 2 セット ~6.7% → run409A heavy で ~10.0% 高位候補上昇 → run410 散発減弱で ~8.3% に収束 (深夜帯 traffic 最低帯での cold 4 セット連続出現は純 traffic 依存説への反証継続; 23時台 (9/7) ~11.3% 高位帯との帯跨ぎ高低差縮小方向)。全セット「帯内 1 窓即消失」散発型継続で heavy 帯水準持続性は単一窓非持続のまま — 帯水準確定・機構判断には rank 追加 n を要する。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (qualify する新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・0hr 4 セット中位帯候補確定間, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 0時台 ~8.3% は順位を変えない)。secret は一切記録せず。NEXT: K-Z3 1時台帯初計測 run411 使用 (0時台 4 セット 20/240 ~8.3% 中位帯候補完了 — 帯水準確定に追加 n が必要だが深夜帯実測は生産性限界のため次の観測枠 1時台帯初 n=1 セットへ移行; falsify/bench が実施, host load gate 超過時は production HTTP フォールバックの従来手順 — K-S1/K-S2 は host quiet 時に KOTOBASE_PACK_WRITES on/off local test の再試行余地あり)。\n"

anchor = "## Iteration log\n- 2026-09-08: **bench 第185回**"
if anchor not in content:
    raise SystemExit("ANCHOR NOT FOUND")

# consume header + first entry start, re-emit header once before new entry
new_content = content.replace(anchor, "## Iteration log\n" + new_entry + "- 2026-09-08: **bench 第185回**", 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

# verify
cnt_header = new_content.count("## Iteration log")
with io.open(path, "r", encoding="utf-8") as f:
    head = f.read(1200)
print("header_count=", cnt_header)
print("entry_present=", "rank 第175回" in new_content)
print("---HEAD1200---")
print(head[:1200])
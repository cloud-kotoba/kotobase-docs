#!/usr/bin/env python3
import io, sys

MD = "query-cosientist.md"
HEADER = "## Iteration log\n"
# The current first iter-log entry (must be re-anchored at insert time)
ANCHOR_PREFIX = "## Iteration log\n- 2026-09-07: bench 第177回。20:58 JST tick。"

entry = """- 2026-09-07: rank 第169回。21:08 JST tick。HEAD 775462d = bench 第177回 (20:58, K-Z3 20時台 run396 cold 3/60) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 6.50–14.65 (21:03 pre-run uptime 実測, gate 7.5 超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (bench 第177回, run396 済)「委ねる (falsify/bench フォールバックは K-Z3 現在時刻帯 20時台 n 積み増し続行、次 run ID は run397 使用 — ※sibling falsify/cosientist 分は同一帯 independent 計測のため rank 判定の取込対象)」。rank 第168回 (0ca3490, 20:39) 以降の新規確定 evidence は 3 commit/窓すべて K-Z3 20時台 n 積み増し: (1) falsify 第169回 355575f run395A–C (20:52, n-add): cold(>=0.5s) 5/2/0 per 20 = 7/60 (~11.7%) — run395A 散発クラスタ 5/20 + run395B 散発 2/20, C+control 0/40 完全静穏分離成立, run394A 単発 1/20 (20:22) の 30 分後再上振れ (heavy>=6/20 未達)。(2) cosientist 第128回 0e98d28 run395A–C (20:2x, independent, run395 は falsify 第169回 と ID 衝突の独立 2 計測): cold 0/60 完全静穏 (search/control とも 0 cold) — run395 全 0/60 は run392A heavy 6/20 → run393A 2/20 → run394A 1/20 の順次減弱の減衰終点として整合, sibling 3 セット (10/180) に対する独立 4 セット目。(3) bench 第177回 775462d run396A–C (20:58, n-add): cold 3/60 (~5.0%) — run396A 冒頭集中 3/20 (1.11/1.27/2.07s), B/C+control 0/40 完全静穏分離成立, falsify run395A+B 7/60 (20:52) の 6 分後散発減弱。取り込み判定: (a) K-Z3: falsify-run395 + cosientist-run395(独立) + run396 を取込、20時台 (9/7) 通算 = run392 7/60 + run393 2/60 + run394 1/60 + falsify-run395 7/60 + cosientist-run395 0/60 + run396 3/60 = 20/360 (~5.6%) の 6 セット中位〜低位帯候補 — 19hr (~8.0%)・18hr (~7.3%)・17hr (~7.5%) と同水準〜やや低位の帯横断継続 (日中帯 traffic 依存説の方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。帯内変動は run392A heavy 6/20 → run393A 2/20 → run394A 1/20 → falsify-run395 7/60 (再上振れ) → cosientist-run395 0/60 → run396A 3/20 の順次減弱・再上振れ共存で「帯内 1 窓即消失」散発クラスタ型継続 — heavy(>=6/20) は falsify-run395 で再達せず (A/B 散発 7/60), heavy 帯水準持続性は単一窓非持続のまま再現未確認。6 セット中 control は全セット 0/20 完全静穏分離成立・cold 群は search 側局在。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (qualify する新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・6 セット中位〜低位帯候補確定間, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 20時台通算 20/360 ~5.6% は順位を変えない)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) に falsify 169 + cosientist 128 + bench 177 を追記済み。NEXT: 委ねる (rank 指定優先; falsify/bench フォールバックは K-Z3 現在時刻帯 21時台帯初計測 (20時台 6 セット 20/360 ~5.6% 中位〜低位帯候補で帯 n 充足・帯水準確定のため次の観測枠 21時台帯初へ移行), 次 run ID は run397 使用)。"""

with io.open(MD, "r", encoding="utf-8") as f:
    txt = f.read()

if txt.count(HEADER) != 1:
    print("ABORT: header count = %d (expected 1)" % txt.count(HEADER))
    sys.exit(2)
if ANCHOR_PREFIX not in txt:
    print("ABORT: anchor prefix not found. First iter line:")
    print(repr(txt[txt.index(HEADER):txt.index(HEADER)+160]))
    sys.exit(3)

new = txt.replace(ANCHOR_PREFIX, HEADER + entry + ANCHOR_PREFIX[len(HEADER):], 1)
with io.open(MD, "w", encoding="utf-8") as f:
    f.write(new)
print("OK inserted. header count now =", new.count(HEADER))
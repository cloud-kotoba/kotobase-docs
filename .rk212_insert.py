#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

entry = (
"- 2026-09-08: rank 第212回。16:07 JST tick。HEAD b3abd65 = bench 第208回 "
"(16:04, K-Z3 16時台帯初計測 run479 cold 6/60 ~10.0% — run479A 散発クラスタ 5/20 "
"+ B 単発, control 0/20 完全静穏分離成立) = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; "
"※本 tick 開始時 worktree に sibling bench 第208回 (run479, 16:06) の未 commit iter-log 編集が在り "
"git diff 非 empty — 挿入・上書きせず ~30-60s 待機+再 fetch で bench 第208回 commit (b3abd65) 着弾・"
"diff empty 化を確認の上 b3abd65 上へ単一 rank 行のみ挿入, header=1 事前確認済; "
"terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由; pre-run monitor NEXT"
"「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — "
"true progressive NEXT は iter-log HEAD 連鎖 (bench 第208回 NEXT フォールバック"
"「K-Z3 現在時刻帯 16時台 n 積み増し続行」))。live smoke 200 (/, /signup; pre-run 計測)。"
"host load1 45.26 (16:10 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。"
"rank 第211回 (04fdafd, 14:14) 以降の新規確定 evidence は 8 commit (すべて K-Z3 日中帯): "
"(a) 14時台: bench 第196回 run472 (5/60) + bench 第197回 run473 (8/60, run473A heavy 6/20 14時台初) "
"+ falsify 第213回 run474 (3/60) → 14時台通算 = run470(5/60帯初)+run471(1/60)+run472(5/60)+"
"run473(8/60)+run474(3/60) = 22/300 (~7.3%) 5セット中位帯候補。"
"(b) 15時台: bench 第206回 run475帯初 (7/60, run475A heavy 6/20) + cosientist 第143回 run476 (5/60) "
"+ bench 第207回 run477 (7/60, run477A heavy 6/20) + falsify 第214回 run478 (2/60) → 15時台通算 "
"= 21/240 (~8.8%) 4セット中〜高位帯候補。(c) 16時台: bench 第208回 run479帯初 (6/60, "
"run479A 散発クラスタ 5/20 + B 単発) → 16時台帯初 6/60 (~10.0%) n=1。取り込み判定: "
"K-Z3 open 継続 — 14時台 22/300 ~7.3%・15時台 21/240 ~8.8%・16時台帯初 6/60 ~10.0% の日中帯 high 側継続 "
"(15時台帯初 7/60→5/60→7/60(heavy)→2/60 の振幅 + 16時台帯初再上振れ 6/60), heavy>=6/20 は "
"run475A/477A で出現するも B/C 0/20 即消失で帯水準として持続せず「帯内 1 窓即消失」散発型継続、"
"traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。各帯 n=1-5 セットで"
"帯水準確定・機構判断には未達 (日中帯 high 側は帯初再上振れ + 帯内散発減衰の繰り返しで帯水準流動的)。"
"K-Q1: 変動なし (残余切れ手は cosientist 実装専任の動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持)。"
"K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす決定的支持/反証に未達 "
"— K-Z3 open 継続・帯水準確定未達, K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 は evidence なし)。"
"新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし "
"(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 現在時刻帯 16時台 n 積み増し継続 "
"(次 run ID run480 — 帯初 n=1 セットのみで帯水準確定未達, falsify/bench が実施)。"
)

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Find the Iteration log header (must be exactly once)
hdr = "## Iteration log\n"
idx = content.find(hdr)
if idx < 0:
    sys.exit("iterlog header not found")

# Verify header count == 1
if content.count(hdr) != 1:
    sys.exit("iterlog header count != 1")

# Insert the new entry right after the header line, preserving the header once.
insert_at = idx + len(hdr)
new_content = content[:insert_at] + entry + "\n" + content[insert_at:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("inserted ok; new size chars=%d" % len(new_content))
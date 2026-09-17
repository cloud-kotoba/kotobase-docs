#!/usr/bin/env python3
import sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ENTRY = ("- 2026-09-08: rank 第179回。03:30 JST tick。HEAD 848788b = falsify 第183回 (03:28, K-Z3 3時台帯初 run418 evidence append) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 16.72 (03:29 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD (falsify 第183回, 03:28) の続行枠。rank 第178回 (02:30) 以降の新規確定 evidence は 3 commit、すべて K-Z3: (1) bench 第187回 run416 (923ddd8, 02:33, 2時台): cold 0/60 完全静穏 — run414 (0/60) に続く 2時台完全静穏 2 セット目, run413A heavy 6/20 の 25 分後完全減衰, control clean 分離成立, heavy>=6/20 再達せず。(2) falsify 第184回 run417 (923ddd8, 02:49, 2時台 n-add): cold 2/60 ~3.3% — run417A 単発散発 1.5109s / run417B 単発散発 0.9214s, C 0/20, control clean 完全静穏分離成立, run414/415/416 完全静穏 3 連続後の散発単発再出現,「帯内 1 窓即消失」型継続 (heavy>=6/20 は run413A 以降 4 セット非再現)。(3) falsify 第183回 run418 (848788b, 03:28, 3時台帯初): cold 4/60 ~6.7% — run418A 散発 3/20 (1.6276s/0.8809s/0.7999s) + run418B 単発 1/20 (0.7734s), C 0/20, control clean 完全静穏分離成立, cold 群 search 局在,「帯内 1 窓即消失」散発単発/ペア型継続 (heavy>=6/20 再達せず)。取り込み判定: (a) K-Z3: run416 + run417 + run418 を取込、2時台 (9/8) 通算 = run413 (6/60, 帯初) + run414 (0/60) + run415 (0/60) + run416 (0/60) + run417 (2/60) = 8/300 (~2.7%) の 5 セット低位帯候補; 3時台 (9/8) 帯初 = run418 4/60 (~6.7%) の 1 セット低〜中位帯候補。9/8 深夜帯は 0時台 20/240 ~8.3% mid → 1時台 7/120 ~5.8% → 2時台 8/300 ~2.7% → 3時台帯初 4/60 ~6.7% の低〜中位帯候補継続 (9/7 深夜帯 ~2.5% 低位帯残界と整合方向) — 深夜帯 traffic 最低帯での cold 散発再出現継続は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンとの対比不変, heavy>=6/20 の帯水準持続性は非持続のまま — バンド水準確定・機構判断には rank 追加 n を要する)。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯水準確定に未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 2時台 ~2.7% / 3時台帯初 ~6.7% は順位を変えない)。secret は一切記録せず。NEXT: K-Z3 現在時刻帯 (3時台) n 積み増し継続 (3時台帯初 4/60 ~6.7% 低〜中位帯候補の帯水準確定・9/8 深夜帯の帯水準確定に追加 n が必要 — cron 実行時刻が 3時台帯内のため 3時台 n-add として実施, 既に 4時台へ移行していれば現時刻帯で実施), 次 run ID は run419 使用。")

HEADER = "## Iteration log"
ANCHOR = HEADER + "\n"

with open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

# safety: exactly one Iteration log header
n_header = content.count(HEADER)
if n_header != 1:
    print("ABORT: header count = %d (expect 1)" % n_header)
    sys.exit(1)

# anchor must immediately precede the current head entry (falsify 第183回)
head_marker = "- 2026-09-08: **falsify 第183回**。03:28 JST tick,HEAD 923ddd8"
if ANCHOR + head_marker not in content:
    print("ABORT: head-marker not directly after header")
    sys.exit(1)

new_content = content.replace(ANCHOR + head_marker,
                              ANCHOR + ENTRY + "\n" + head_marker, 1)

if new_content == content:
    print("ABORT: no change made")
    sys.exit(1)

with open(PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

# verify
with open(PATH, "r", encoding="utf-8") as f:
    check = f.read()

print("OK header=%d rank179_present=%s head_marker_order=%s" % (
    check.count(HEADER),
    "rank 第179回" in check,
    check.find(HEADER) < check.find(head_marker) < check.find("rank 第179回")
))
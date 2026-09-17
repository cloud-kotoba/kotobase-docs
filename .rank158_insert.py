#!/usr/bin/env python3
import sys, io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

# sanity: exactly one iteration-log header
hdr = "## Iteration log"
assert content.count(hdr) == 1, "header count = %d" % content.count(hdr)

anchor = "## Iteration log\n- 2026-09-07: falsify 第168回"
assert content.count(anchor) == 1, "anchor count = %d" % content.count(anchor)

entry = (
"- 2026-09-07: rank 第158回。15:46 JST tick。HEAD 8db0901 = remote net-kotobase/main 一致 "
"(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取込; "
"terminal foreground 出力不可=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。"
"host load1 57.18 (15:25 pre-run uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。"
"※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — "
"true progressive NEXT は falsify 第168回 (iter-log, 15:34)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 15時台 n 積み増し続行、次 run ID は run368 使用)」。"
"rank 第157回 (13cbce4, 14:59, fold falsify165-run361 + falsify166-run362 + bench157-run363 -> 14時台 19/300 ~6.3% 5-set) 以降の新規確定 evidence は 4 commit、すべて K-Z3 15時台: "
"(1) falsify 第167回 run365 (19f7324, 15時台帯初, cold 0/60 完全静穏 — bench 第158回 run364 (0/60, 15:12) を coherent superset として同一 commit に sweep), "
"(2) bench 第159回 run366 (db5c58c, 15:26, cold 5/60 ~8.3% — run366A 散発 4/20 (1.4244/1.1564/1.0457/1.9573s idx1/6/7/8), run366B 単発 1/20, run366C 0/20, control 0/20 完全静穏分離成立), "
"(3) falsify 第168回 run367 (e7e80ca, 15:34, cold 4/60 ~6.7% — run367A 散発 3/20 (1.1006/1.0579/0.9655s idx2/4/12), run367B 0/20, run367C 単発 1/20 (0.9980s idx5), control 0/20 完全静穏分離成立), "
"(4) bench 第91回 (8db0901, 15:40, 測定なし — 15時台帯完了・次の観測枠 16時台未着のため, host busy load1 27.50 記録のみ)。"
"取り込み判定: (a) K-Z3: run364+run365+run366+run367 を取込、15時台 (9/7) 通算 = 9/240 (~3.8%) の 4 セット低位帯。"
"帯初 2 セット (run364+run365) 完全静穏 → run366A 4/20 散発再出現 → run367 4/60 散発継続で「帯内 1 窓即消失」散発即消失型が 15時台でも維持 "
"(heavy>=6/20 は再達せず, run331A 9/20 heavy 型の帯水準持続性は再現未確認)。"
"15時台 ~3.8% は 14時台 (~6.3%)・13時台 (~4.0%)・12時台 (~6.9%)・11時台 (~6.4%) より低位の低位帯で日中帯 traffic 依存説の方向支持継続 "
"(深夜帯 ~26-31% 平坦パターンとの対比不変)。帯完了 4 セット・帯水準は低位帯として確定寄りだが、機構判断 (time-traffic 依存 vs 非依存) の確定は 16時台以降の time-band 横断 n を要する。"
"(b) K-Q1: 変動なし (transact 401 静的切れ手全棄却済み、残余は cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ、KV read 内訳初実測滞留継続、最上位維持)。"
"(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。"
"status 遷移なし (transition 要件を満たす新 evidence なし: K-Z3 は観測継続・機構判断未達, K-Q1 は cosientist 実装待ち, K-Z2/K-S1/K-S2 は evidence なし)。"
"新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。"
"rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 15時台 ~3.8% 低位帯は周辺帯と同系の継続観測で rank 入れ替えに至る差ではない)。"
"secret は一切記録せず。"
"NEXT: K-Z3 16時台帯初計測、次 run ID は run368 使用 (15時台 4 セット 9/240 ~3.8% 低位帯完了 — 実行時刻 15:46 JST は 15時台終盤, 16時台移行後は帯初計測に最短 1 セット)。\n"
)

new_content = content.replace(anchor, "## Iteration log\n" + entry + "- 2026-09-07: falsify 第168回", 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

# verify
with io.open(path, "r", encoding="utf-8") as f:
    chk = f.read()
assert chk.count("## Iteration log") == 1, "post header count = %d" % chk.count("## Iteration log")
assert "rank 第158回" in chk
assert chk.index("rank 第158回") < chk.index("falsify 第168回")
print("OK inserted rank 第158回, header count =", chk.count("## Iteration log"))
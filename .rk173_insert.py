#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

header = "## Iteration log\n"
assert text.count(header) == 1, "header count = %d" % text.count(header)

new_entry = ("- 2026-09-07: rank 第173回。23:57 JST tick。HEAD e2a082a = falsify 第177回 (23:32, "
    "K-Z3 23hr n-add run405 cold 11/60 ~18.3%) = remote net-kotobase/main 一致 (git fetch + rev-parse "
    "比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため"
    "状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 6.97 "
    "(23:48 pre-run, gate 7.5 未満) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT"
    "「K-Z3 深夜帯 23時台 n 積み増し続行」は stale (rank 第90回帯 artifact) — true progressive NEXT は "
    "iter-log HEAD (falsify 第177回, run405 済)「委ねる (rank 指定優先; フォールバックは 現在時刻帯 23時台"
    " n 積み増し続行、次 run ID は run406 使用)」。rank 第172回 (11f80c8, 23:04) 以降の新規確定 evidence は "
    "1 commit、すべて K-Z3: falsify 第177回 run405A-C (23時台 n-add, 23:32): cold 11/60 ~18.3% — run405A "
    "cold 7/20 heavy 散発クラスタ (deep 2.48s 含む) p50 100.4ms / run405B 単発 1/20 / run405C 境界 3/20, "
    "control cold 3/20 境界値 not-separated-leaning (search cold 405A deep で magnitude 分離弱成立だが "
    "control 境界 3 件で完全静穏でない)。取り込み判定: (a) K-Z3: run405 を取込、23時台 (9/7) 通算 = run403 "
    "(7/60) + run404 (3/60) + run405 (11/60) = 21/180 (~11.7%) で 22時台 (17/120 ~14.2%) と同水準の高位帯"
    "継続 — 21時台 (~6.3%)・20時台 (~5.6%) より明確に高位の夜帯 traffic 遷移説弱支持継続 (日中低位帯 ~2-7% "
    "との対比顕著; 深夜帯 ~26-31% 平坦パターンとの対比不変)。ただし 23時台 3 セット中 run404/run405 は "
    "control borderline/not-separated-leaning のため band 高位確定・機構判断には未達 — 追加 clean-tick n "
    "を要する。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合のみ, 最上位維持。(c) "
    "K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: "
    "K-Z3 は観測継続で 23時台 高位が corroborate されたが control not-separated-leaning のため決定的でない)。"
    "新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > "
    "K-S1 > K-S2 — 23時台 ~11.7% 高位は K-Z3 観測継続のままで順位を変えない)。secret は一切記録せず。NEXT: "
    "K-Z3 23時台 n 積み増し継続 (23時台 21/180 ~11.7% 高位; run404/405 control borderline のため追加 "
    "clean-tick n 推奨 — quiet-host に clean control 分離成立セットを積む)、次 run ID は run406 使用。")

# Anchor: consume header + immediately following first-entry line, re-emit header once + new entry
new_text = text.replace(header + "- 2026-09-07: ", header + new_entry + "\n- 2026-09-07: ", 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_text)

# verification output
print("header_count_after:", new_text.count("## Iteration log"))
print("new_entry_present:", "rank 第173回" in new_text)
print("first_entry_still_present:", "falsify 第177回" in new_text)
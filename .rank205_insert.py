#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
new_entry = (
    "- 2026-09-08: rank 第205回。12:04 JST tick。HEAD 05b9138 = rank 第204回 (11:50, "
    "fold run460+461 -> 11時台 13/300 ~4.3% 5セット: 9時台 11/300 ~3.7%・10時台 17/420 "
    "~4.0% と同水準の日中帯低〜中位帯継続, control 完全静穏分離成立, heavy>=6/20 非再現継続) "
    "= remote bench_fetch/main 一致 (git fetch + rev-parse 比較, 乖離 0; worktree detached "
    "HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。"
    "live smoke 200 (/,/signup; pre-run 計測)。host load1 8.49 (12:02 uptime 実測, gate 7.5 超過) "
    "- rank は測定しない (状態正本の更新のみ) ため影響なし。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 "
    "深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) - true progressive NEXT は iter-log "
    "HEAD (rank 第204回, 05b9138, 11:50)「K-Z3 11時台 n-add run462」。rank 第203回 (6a924be) は前 tick で "
    "取込済み・以降の新規確定 evidence は 0 commit (HEAD=rank 第204回自身の commit で advance 完了, bench/"
    "falsify/cosientist の新 commit なし) — 取り込むべき測定量なし。time band 現況: 現在時刻 12:04 で 12時台 "
    "(9/8) 帯内、11時台帯は rank 第204回で 13/300 通算 5 セット確定 (帯水準は低〜中位帯候補のまま・機構判断 "
    "に未達)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装専任の動的照合 "
    "のみ・KV read 内訳初実測滞留, K-Z3 は観測継続・帯確定未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。"
    "evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。"
    "secret は一切記録せず。NEXT: K-Z3 12時台帯初計測 run462 (11時台 13/300 ~4.3% 5セット低〜中位帯候補で帯完了"
    " — 次の観測枠 12時台帯初 n=1 セットを falsify/bench が実施, run462 使用; 帯水準確定・機構判断は "
    "12時台追加 n + 帯横断 n 待ちのまま)。"
)

with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

header = "## Iteration log"
first_entry = "- 2026-09-08: rank 第204回"
idx = text.find(header + "\n" + first_entry)
if idx < 0:
    print("ANCHOR_NOT_FOUND")
    sys.exit(2)

# Verify we consumed the header once and it's unique
hdr_count = text.count("## Iteration log")
if hdr_count != 1:
    print("HDR_COUNT=%d (expected 1)" % hdr_count)
    sys.exit(3)

insert_at = idx + len(header) + 1  # after header newline
new_text = text[:insert_at] + new_entry + "\n" + text[insert_at:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_text)

# verification
with io.open(path, "r", encoding="utf-8") as f:
    check = f.read()
print("HDR_NOW=", check.count("## Iteration log"))
print("RANK205_PRESENT=", "- 2026-09-08: rank 第205回" in check)
print("ORDER205_BEFORE_204=", check.find("rank 第205回") < check.find("rank 第204回"))
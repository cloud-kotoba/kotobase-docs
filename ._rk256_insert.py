import io
import re

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    text = f.read()

headers = [m.start() for m in re.finditer(r"(?m)^## Iteration log$", text)]
assert len(headers) == 1, "header count != 1: %d" % len(headers)

entry = (
    "- 2026-09-09: rank 第256回。19:02 JST tick。HEAD f35abbd = 自 rank 第255回 (15:02 tick) = fetch 後 net-kotobase/main・bench_fetch/main 先端一致 (fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; '## Iteration log' ヘッダ 1 件・worktree diff HEAD 空・rank 第256回 entry 不在を事前確認; terminal foreground stdout 空=既知のため状態確認はファイル書出経由; pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第255回 NEXT「K-Z3 15時台帯初計測 run572」))。rank 第255回 (f35abbd, 15:02) 以降の新規確定 evidence は 0 本 — 15:02–19:02 JST の 4 時間 sibling commit なし (falsify/bench/cosientist とも run572 枠を未消化、15/16/17/18時台 (9/9) は全帯未計測のまま経過し帯欠測。14時台 (9/9) に続き 15–18時台も欠測注記; 16時台 (9/8) run479–483 ~8.3%・17時台 (9/8) 12/120 ~10.0% は前日実績で別帯)。取り込み判定: (a) K-Z3: fold 対象なし — 13時台 (9/9) 通算 14/420 (~3.3%) 7 計測確定 (rank 第255回) を維持したまま日中帯帯間勾配の 15–18時台データが丸ごと欠落。現在 19時台のため 15時台待機は不可能 (falsify run275/cosientist run105 precedent に従い現時刻帯を優先) — 夜帯 (19–22時台) の帯水準は 9/6 実績 (19時台 ~6.7%・21時台 ~4.0%・22時台 ~12.5%) と 9/8 (21時台 ~10.8%・22時台 ~11.7%) で夜帯中〜高位帯候補だが 9/9 分はゼロ。K-Z3 traffic 依存説の日中帯方向支持は継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。(b) K-Q1: 変動なし — cacao_b64 harness 変更は host load1 23.83–25.68 (19:02 pre-run monitor 実測, gate 7.5 大幅超過) で local 測定不可のまま低負荷 tick 待ち, 最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (新規 evidence ゼロのため判定材料なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。live smoke 200 (/, /signup; pre-run monitor 計測)。secret は一切記録せず。NEXT: K-Z3 19時台帯初計測 (15:02 以降 sibling run が停滞し 15–18時台が帯欠測のまま 19時台へ到達したため、現時刻帯の夜帯起点データ取得が最優先; 9/6 19時台 run234 4/60 ~6.7%・9/8 21時台 ~10.8% と夜帯中位〜高位帯候補だが 9/9 分はゼロ), 次 run ID は run572 使用 (run572 は rank 第255回 NEXT で指定済みだが未消費のためそのまま使用)。\n"
)

anchor_line = "- 2026-09-09: rank 第255回。15:02 JST tick。"
idx = text.index("## Iteration log\n")
first_entry_start = idx + len("## Iteration log\n")
assert text.startswith(anchor_line, first_entry_start), "first entry is not rank 255th"

new_text = text[:first_entry_start] + entry + text[first_entry_start:]
assert len([m for m in re.finditer(r"(?m)^## Iteration log$", new_text)]) == 1
assert "rank 第256回" in new_text
with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_text)
print("inserted ok")

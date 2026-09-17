# -*- coding: utf-8 -*-
# Insert bench 第178回 iter-log entry after '## Iteration log' header (before rank 第169回 entry).
path = "query-cosientist.md"
data = open(path, encoding="utf-8").read()
lines = data.split("\n")
assert lines[366] == "## Iteration log", "L367 header mismatch"
new_entry = (
    "- 2026-09-07: bench 第178回。21:11 JST tick。HEAD de436f4 = rank 第169回 (21:13, K-Z3 20hr"
    " 6-set 20/360 ~5.6% fold, NEXT「K-Z3 21hr band-first run397」) = remote net-kotobase/main 一致"
    " (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため git pull --ff-only 不可,"
    " fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・計測出力はファイル書き出し経由)。"
    " live smoke 200 (/, /signup; pre-run 計測)。host load1 35.7–39.0 (21:11 uptime 実測, gate 7.5"
    " 大幅超過) のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    " ※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) —"
    " true progressive NEXT は iter-log HEAD (rank 第169回, de436f4)「K-Z3 21hr band-first run397」の"
    " run397 枠を本 tick 実施 (21時台帯初計測, 20時台 run392..396 完了後の帯移行, .b397 既存なし=衝突なし確認)。"
    " K-Z3 21時台 run397A–C 実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s,"
    " nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 21:11:27–21:11:45 JST,"
    " 全 80/80 200, secret 不含 — curl + python stats のみ): cold(>=0.5s) 0/1/2 per 20 = 3/60 (~5.0%)"
    " — run397A cold 0/20 p50 0.076s / run397B cold 単発 1/20 (1.1255s pos1) p50 0.060s / run397C"
    " cold 2/20 (0.5752s pos15 / 0.9290s pos19) p50 0.119s, control (kotobase.net/signup) cold 1/20"
    " (0.5023s 境界値) p50 0.120s max 0.502s で control に cold 境界 1 件出現 → borderline"
    " not-separated-leaning (search cold 3/60 のうち 1.13s/0.93s は閾値決定的, host load 35-39 p50 上振れ込みで弱い)。"
    " 21時台帯初 cold 3/60 ~5.0% は 20時台 (20/360 ~5.6% 6-set)・19hr (~8.0%) と同水準の中位〜低位帯候補、"
    " 日中帯 traffic 依存説の方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。帯初 n=1 セットで"
    " 帯水準確定・機構判断には rank 追加 n を要する (not-separated-leaning のため追加 clean-tick n 推奨)。"
    " status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。secret は一切記録せず。"
    " NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 21時台 n 積み増し続行"
    " (帯初計測 run397 済みの積み増し)、次 run ID は run398 使用 — ※sibling falsify/cosientist 分は"
    " 同一帯 independent 計測のため rank 判定の取込対象)。"
)
lines[367:367] = [new_entry]
open(path, "w", encoding="utf-8").write("\n".join(lines))
print("iter-log entry inserted; new line 368 starts:", repr(lines[368][:60]))
print("new total lines:", len(lines))
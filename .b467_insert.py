#!/usr/bin/env python3
# bench tick: append run467 evidence to K-Z3 row end + insert iter-log entry
import io, sys

FN = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(FN, "r", encoding="utf-8") as f:
    lines = f.readlines()

# ---- 1. locate ## Iteration log header ----
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "iter header not found"
assert hdr_idx >= 1, "header position unexpected"

# ---- 2. evidence tail = line just before header (continuation of K-Z3 row) ----
ev_idx = hdr_idx - 1
ev_tail = lines[ev_idx]
assert ev_tail.lstrip().startswith("bench 2026-09-08") or ev_tail.lstrip().startswith("falsify"), \
    "expected K-Z3 evidence continuation line before header, got: " + ev_tail[:60]

ev_text = (
    " bench 2026-09-08 (第193回, K-Z3 13時台帯初計測 run467A\u2013C \u2014 "
    "rank 第208回 NEXT\u300cK-Z3 13時台帯初計測 run467\u300dどおり "
    "(12時台 5 セット確定後、cron 実行時刻 13:24 が 13時台へ帯移行済みのため 13時台帯初計測として実施, "
    "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test + landing kotobase.net/signup, "
    "13:24\u201313:25 JST, 全 80/80 200, host load1 106.79 (13:24 uptime 実測, gate 7.5 大幅超過) "
    "は production HTTP 実測のため gate 外, secret 不含 \u2014 curl + python stats のみ): "
    "cold(>=0.5s) 8/0/0 per 20 = 8/60 (~13.3%) \u2014 run467A heavy 寄り散発クラスタ 8/20 "
    "(1.1875s 1番目 / 1.9072s 2番目 / 1.2331s 3番目 / 1.8686s 4番目 / 1.2872s 7番目 / "
    "1.3908s 11番目 / 1.2620s 14番目 / 1.5814s 19番目 \u2014 冒頭 4 連続 + 中盤以降散発 4 件, "
    "warm 群 0.076\u20130.346s で cold と交互) p50 253.8ms / run467B cold 0/20 p50 207.4ms max 458.0ms / "
    "run467C cold 0/20 p50 105.2ms max 270.4ms, control (kotobase.net/signup) cold 0/20 p50 71.6ms "
    "max 170.5ms 完全静穏で control 分離成立、cold 群は search 側に局在。run467A cold 8/20 は B/C 0/40 + "
    "control 0/20 で即消失し \u300c帯内 1 窓即消失\u300d heavy 寄り散発クラスタ型 (run271A 8/60 帯初 heavy 型の弱い再現, "
    "run462A 12時台帯初 8/20 と同型の重い朝→昼境再上振れ) \u2014 13時台帯初計測で heavy->6/20 (8/20) が "
    "12時台帯初 (8/20) と同水準で再現し、12時台 n 積み増し 3 セット (run463-465, cold 3+3+4 = 10/180) の "
    "散発減衰から帯初 1 窓 heavy への再上振れが帯移行時に繰り返すパターンを支持。13時台 (9/8) 帯初計測 "
    "cold 8/60 ~13.3% は日中帯高水準 (\u224812時台帯初 13.3%) で、低位帯 (6-7時台 ~1.7-2.2%) との差は "
    "入れ替わりが帯初に集中するパターンと整合し K-Z3 traffic 依存説の方向支持を継続。host load1 106 高騰の "
    "p50 全体的上振れ込み borderline note 付き (cold 8 件 1.19\u20131.91s は閾値決定的, control 完全静穏)。"
    "status 判定は rank に委ねる (rank 専門)。"
)

# append to evidence tail line
new_ev = ev_tail.rstrip("\n") + ev_text + "\n"
lines[ev_idx] = new_ev

# ---- 3. insert iter-log entry right after header ----
ilog_entry = (
    "- 2026-09-08: bench 第193回。13:28 JST tick。HEAD 9532f63 = rank 第208回 (13:20, "
    "K-Z3 12時台 18/300 ~6.0% 5 セット fold; NEXT K-Z3 13時台帯初計測 run467) = remote "
    "net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため "
    "fetch 系で取込; worktree diff HEAD -- query-cosientist.md は空 (クリーン) を事前確認; "
    "terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; "
    "pre-run monitor NEXT\u300c委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。\u300dは stale "
    "(rank 第90回帯 artifact) \u2014 true progressive NEXT は iter-log HEAD 連鎖)。rank 第208回 "
    "NEXT\u300cK-Z3 13時台帯初計測 run467\u300dに従い run467A\u2013C を 13時台帯初計測として実施 "
    "(12時台 5 セット確定後、cron 実行時刻 13:24 が 13時台へ帯移行済みのため現時刻帯で帯初計測, "
    "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 13:24\u201313:25 JST, 全 80/80 200, "
    "host load1 106.79 (13:24 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外): "
    "cold 8/0/0 per 20 = 8/60 (~13.3%) \u2014 run467A heavy 寄り散発クラスタ 8/20 "
    "(1.19\u20131.91s, 冒頭 4 連続 + 中盤以降散発 4 件, 詳細は K-Z3 evidence 欄 L279 末尾追記), "
    "B/C 0/40 即消失, control 0/20 完全静穏で control 分離成立。13時台帯初計測 cold 8/60 ~13.3% は "
    "12時台帯初 (8/20 ~13.3%) と同水準の重い再上振れで、低位帯 (6-7時台) との入れ替わりが帯初に集中する "
    "パターンを継続し K-Z3 traffic 依存説の方向支持を維持 (深夜帯 ~26-31% の対比は不変)。host load 高騰の "
    "p50 上振れ borderline note 付きだが cold 8 件 1.19\u20131.91s は閾値決定的。status 遷移なし "
    "(rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 "
    "n 積み増し, 次 run ID は run468)。\n"
)

lines.insert(hdr_idx + 1, ilog_entry)

# ---- write back ----
with io.open(FN, "w", encoding="utf-8", newline="\n") as f:
    f.writelines(lines)

print("done: ev_idx=", ev_idx, "hdr_idx=", hdr_idx)
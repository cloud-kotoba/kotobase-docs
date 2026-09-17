#!/usr/bin/env python3
# Append run403 evidence to K-Z3 row (L279 END) and insert iter-log entry (newest-first after header L369).
import sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

# scrub zero-width chars / problematic tokens per memory
for c in ["\u200b", "\u200c", "\u200d", "\ufeff"]:
    txt = txt.replace(c, "")

lines = txt.split("\n")

# sanity: locate K-Z3 row (line index 278 = L279) and iter-log header (line index 368 = L369)
assert lines[278].startswith("| K-Z3 | worker |"), "K-Z3 row not at L279: %r" % lines[278][:40]
assert lines[368].strip() == "## Iteration log", "Iteration log header not at L369: %r" % lines[368][:40]

ev = (" falsify 2026-09-07 (第176回, K-Z3 23時台帯初計測 run403A\u2013C \u2014 iter-log HEAD (bench 第182回) "
 "「委ねる ... 次 run ID は run403 使用」の run403 枠 (cron 実行時刻 23:04 が 23時台へ帯移行、22時台 run401/402 17/120 ~14.2% 完了後の 23時台帯初計測), "
 "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 23:04:07\u201323:04:26 JST, "
 "全 80/80 200, host load1 15.59\u219217.10 (23:04 uptime 実測, gate 7.5 超過) は production HTTP 実測のため gate 外, secret 不含 \u2014 curl + python stats のみ): "
 "cold(>=0.5s) 7/0/0 per 20 = 7/60 (~11.7%) \u2014 run403A cold 7/20 heavy 散発クラスタ (1.2678s/1.2968s/1.3540s/1.4694s/1.6630s/2.1087s/2.7392s 散発配置, deep cold 2.74s 含む) p50 64.0ms "
 "/ run403B cold 0/20 p50 51.8ms max 242.9ms / run403C cold 0/20 p50 59.4ms max 157.1ms, control (kotobase.net/signup) cold 0/20 p50 53.7ms max 316.6ms "
 "完全静穏で control 分離成立、cold 群は search 側に局在。run403A cold 7/20 heavy (>=6/20 heavy 閾値再達の 23時台帯初, deep 2.74s) は B/C 0/40 + control 0/20 で即消失し "
 "「帯内 1 窓即消失」散発/heavy クラスタ型継続 \u2014 直前 22時台 run402A 頭クラスタ 7/20 (22:31) と同様の night-band heavy 散発クラスタが 33 分後に 23時台帯初でも再現 (両セット 7/20 heavy), "
 "夜帯 traffic 遷移説の弱い支持方向継続。23時台 (9/7) 帯初 = 7/60 (~11.7%) は 9/6 23時台 (30/540 ~5.6%) より高位で、22時台 (17/120 ~14.2%) と同水準の高位帯候補 "
 "(帯 n=1 セットで帯水準確定・機構判断には rank 追加 n を要する)。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 23時台 n 積み増し続行、次 run ID は run404 使用)")

iter_entry = ("- 2026-09-07: **falsify 第176回**。23:04 JST tick。HEAD 966ac7cc = bench 第182回 (22:33, K-Z3 22hr n-add run402 cold 9/60) = remote net-kotobase/main 一致 "
 "(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由)。"
 "live smoke 200 (/, /signup; pre-run 計測 + 本 tick 実測全 80/80 200)。host load1 15.59\u219217.10 (23:04 uptime 実測, gate 7.5 超過) のため local 測定は拒否 \u2014 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
 "※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) \u2014 true progressive NEXT は iter-log HEAD (bench 第182回, 22:33) "
 "「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行、次 run ID は run403 使用)」。cron 実行時刻 23:04 が 22時台 (run401/402 済 17/120 ~14.2%) 完了後の "
 "23時台へ帯移行済みのため run403 を現時刻帯 23時台帯初計測として実施 (.b403 既存なし=衝突なし確認)。run403 実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, "
 "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 23:04:07-23:04:26 JST, 全 80/80 200, secret 不含): cold(>=0.5s) 7/0/0 per 20 = 7/60 (~11.7%) \u2014 "
 "run403A cold 7/20 heavy 散発クラスタ (1.2678s/1.2968s/1.3540s/1.4694s/1.6630s/2.1087s/2.7392s, deep 2.74s 含む) p50 64.0ms / run403B cold 0/20 p50 51.8ms / run403C cold 0/20 p50 59.4ms, "
 "control (kotobase.net/signup) cold 0/20 p50 53.7ms max 316.6ms 完全静穏で control 分離成立、cold 群 search 側局在。run403A cold 7/20 heavy (>=6/20 閾値再達の 23時台帯初) は B/C 0/40 + control 0/20 で即消失し "
 "「帯内 1 窓即消失」型継続 \u2014 22時台 run402A 頭クラスタ 7/20 (22:31) の 33 分後再現で night-band heavy 散発クラスタが帯跨ぎ連続 (両セット 7/20 heavy)、夜帯 traffic 遷移説の弱い支持方向継続。"
 "23時台 (9/7) 帯初 = 7/60 (~11.7%) は 22時台 (17/120 ~14.2%) と同水準・9/6 23時台 (30/540 ~5.6%) より高位の高位帯候補 (帯 n=1 セットで帯水準確定は rank 追加 n 待ち)。"
 "status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。詳細は K-Z3 evidence 欄 (L279 末尾) 追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 23時台 n 積み増し続行、次 run ID は run404 使用)。")

# append evidence to END of K-Z3 row (line index 278)
lines[278] = lines[278] + ev

# insert iter-log entry as a new line right after header (index 369 in new list)
# header was at old index 368; after appending to earlier line, header index unchanged (368).
header_idx = 368  # "## Iteration log"
lines.insert(header_idx + 1, iter_entry)

out = "\n".join(lines)
with open(PATH, "w", encoding="utf-8") as f:
    f.write(out)

print("done; lines now", len(lines))
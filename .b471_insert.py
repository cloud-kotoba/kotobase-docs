#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
raw = open(p, encoding="utf-8").read()
lines = raw.split("\n")

EVID = (
 " bench 2026-09-08 (第195回, K-Z3 14時台 n 積み増し run471A"
 "\u2013C "
 "— falsify 第212回 run470 (14時台帯初) の続行枠 (iter-log HEAD NEXT run471), "
 "同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
 "正 endpoint search.kotobase.net/search?q=test, 14:08"
 "\u201310 JST, 全 80/80 200, host load1 56.83 (14:08 uptime 実測, gate 7.5 大幅超過) "
 "は production HTTP 実測のため gate 外, secret 不含 "
 "\u2014 curl + python stats のみ): "
 "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) "
 "\u2014 run471A 単発散発 1/20 (1.2703s) p50 90.4ms / run471B cold 0/20 p50 74.0ms max 196.4ms "
 "/ run471C cold 0/20 p50 66.8ms max 390.0ms, control (kotobase.net/signup) cold 0/20 "
 "p50 72.1ms max 164.7ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
 "run471A 単発は B/C 0/20 + control 0/20 で即消失し"
 "\u300c帯内 1 窓即消失\u300d散発単発型継続 "
 "(run470A 4/20 散発クラスタ \u2192 本 tick 1/20 散発減衰, heavy>=6/20 は 14時台帯初 5/20 "
 "未達のまま非再現)。14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + 本 tick run471 (1/60) "
 "= 6/120 (~5.0%) の 2 セット"
 " \u2014 帯初再上振れ (run470A 4/20) \u2192 帯内散発減衰 (本 tick 1/20) の 12時台/13時台型 "
 "帯内減衰と同型パターン継続、traffic 依存説の日中帯方向支持継続 "
 "(深夜帯 ~26-31% 平坦パターンとの対比不変)。帯 n=2 セットのみで帯水準確定"
 "\u30fb機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
)

ITER = (
 "- 2026-09-08: bench 第195回。14:08 JST tick。HEAD a610982 = remote net-kotobase/main 一致 "
 "(git fetch net-kotobase main + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; "
 "terminal foreground stdout 空=既知のため状態確認"
 "\u30fb計測出力はファイル書き出し経由; pre-run monitor NEXT"
 "\u300c委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。\u300dは stale (rank 第90回帯 artifact) "
 "\u2014 true progressive NEXT は iter-log HEAD 連鎖 (falsify 第212回 NEXT"
 "\u300c委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run471)\u300d))。"
 "本 tick は falsify 第212回 run470 (14時台帯初, 14:02) に続く 14時台 2 セット目 run471A"
 "\u2013C を実施。live smoke 200 (/, /signup; pre-run 計測)。host load1 56.83 (14:08 uptime 実測, "
 "gate 7.5 大幅超過) のため local 測定は拒否 \u2014 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
 "K-Z3 14時台 run471A"
 "\u2013C を実測 (同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
 "正 endpoint search.kotobase.net/search?q=test, 14:08"
 "\u201310 JST, 全 80/80 200, secret 不含 \u2014 curl + python stats のみ): "
 "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) "
 "\u2014 run471A 単発散発 1.2703s (1/20) p50 90.4ms max 1270.3ms / run471B cold 0/20 p50 74.0ms "
 "max 196.4ms / run471C cold 0/20 p50 66.8ms max 390.0ms, control (kotobase.net/signup) cold 0/20 "
 "p50 72.1ms max 164.7ms 完全静穏で control 分離成立、cold 群は search 側に局在。"
 "run471A 単発は B/C 0/20 + control 0/20 で即消失し"
 "\u300c帯内 1 窓即消失\u300d散発単発型継続 "
 "(run470A 4/20 散発クラスタ \u2192 本 tick 1/20 減衰、heavy>=6/20 は 14時台帯初 5/20 "
 "未達のまま非再現)。14時台 (9/8) 通算 = falsify run470 (5/60, 帯初) + 本 tick run471 (1/60) "
 "= 6/120 (~5.0%) の 2 セット中位帯候補 \u2014 帯初再上振れ \u2192 帯内減衰の日中帯パターン継続、"
 "traffic 依存説の日中帯方向支持継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。帯 n=2 セットで帯水準確定"
 "\u30fb機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
 "詳細は K-Z3 evidence 欄 (L403 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 "
 "現在時刻帯 14時台 n 積み増し続行, 次 run ID は run472)。"
)

# Part 1: append EVID to K-Z3 evidence row (line index 402, the giant accumulation line)
lines[402] = lines[402] + EVID

# Part 2: insert ITER after '## Iteration log' header + blank, before first entry
hdr_idx = None
for i, l in enumerate(lines):
    if l.strip() == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "header not found"
ins_idx = hdr_idx + 1
while ins_idx < len(lines) and lines[ins_idx].strip() == "":
    ins_idx += 1
lines.insert(ins_idx, ITER)

open(p, "w", encoding="utf-8").write("\n".join(lines))
with open("/tmp/b471_insert.txt", "w", encoding="utf-8") as f:
    f.write("hdr_idx=%d ins_idx=%d line403_len=%d\n" % (hdr_idx, ins_idx, len(lines[402])))
print("ok")
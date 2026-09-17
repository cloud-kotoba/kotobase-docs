#!/usr/bin/env python3
# falsify 229: append run516 evidence to L279 tail + insert iter-log row
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

ev = (
    " falsify 2026-09-09 (第229回, K-Z3 0時台(24時台) n 積み増し run516A--C "
    "-- falsify 第228回 NEXT「次 run ID は run516」の run516 枠として実施, 現在帯 0時台(24時台) へ移行済みのため "
    "現時刻帯 0時台 n 積み増し (falsify 第129回 run284 等 precedent), 同測定法 n=20 x 3 + landing control, "
    "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "00:15:3x-00:16:06 JST, 全 80/80 200, host load1 90-136 (00:12/00:15 uptime 実測, gate 7.5 大幅超過) は "
    "production HTTP 実測のため gate 外, secret 不含 -- curl + python stats のみ): "
    "cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) -- run516A 中盤集中クラスタ 5/20 "
    "(pos4 2.0083s + pos7-10 連続 4 件 1.3814/1.4217/1.7193/2.3828s, warm 群 0.09-0.34s と交互) "
    "p50 0.2819s max 2.3828s / run516B cold 0/20 p50 0.1395s max 0.3242s / run516C cold 0/20 p50 0.1329s max 0.1733s, "
    "control (kotobase.net/signup) cold 0/20 p50 0.0619s max 0.2089s 完全静穏で control 分離成立, "
    "cold 群は search 側に局在。run516A 中盤集中 5/20 は B/C 0/40 + control 0/20 で即消失し「帯内 1 窓即消失」型継続 "
    "(heavy>=6/20 は未達, run515A 7/20 (23:52) の ~23 分後 0時台移行直後の弱い再上振れ)。0時台(9/9) 通算 = 本 tick 5/60 (~8.3%) "
    "の 1 セット -- 23時台 (9/8, 23/240 ~9.6%) から 0時台へ移行帯として低温帯でなく中位帯候補, "
    "深夜帯 traffic 最低帯 (0時台) での cold 多発クラスタは K-Z3 traffic 依存説への反証材料を継続 "
    "(深夜帯 ~26-31% 平坦パターンへの遷移は継続観測, heavy>=6/20 は帯水準として持続せず)。帯 n=1 セットで "
    "帯水準確定・機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。"
)
iter_row = (
    "- 2026-09-09: falsify 第229回。00:16 JST tick。HEAD 50870c7 = rank 第224回 (23:59, fold K-Z3 23hr "
    "run514+run515 = 23/240 ~9.6% 4-set; NEXT 委ねる) = remote net-kotobase/main 一致 "
    "(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground "
    "stdout 空=既知のため状態確認・計測出力はファイル書出経由)。pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 "
    "23時台 n 積み増し継続。」は stale (rank 帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 "
    "(falsify 第228回 NEXT「次 run ID は run516」)。live smoke 200 (/, /signup, search.kotobase.net/search?q=test; "
    "本 tick 実測 200 3/3)。host load1 136.00 (00:15 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため "
    "gate 外で実施。K-Z3 0時台(24時台) n 積み増し run516A-C 実測 (同測定法 n=20 x 3 + landing control, "
    "別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "00:15:3x-00:16:06 JST, 全 80/80 200, secret 不含 -- curl + python stats のみ): "
    "cold 5/0/0 per 20 = 5/60 (~8.3%) - run516A 中盤集中クラスタ 5/20 (pos4 2.0083s + pos7-10 連続 4 件 "
    "1.3814/1.4217/1.7193/2.3828s) p50 281.9ms / run516B 0/20 p50 139.5ms / run516C 0/20 p50 132.9ms, "
    "control (kotobase.net/signup) 0/20 p50 61.9ms max 208.9ms 完全静穏で control 分離成立, cold 群 search 側局在。"
    "「帯内 1 窓即消失」型 (A 5/20 即消失, heavy>=6/20 未達), 0時台(9/9) 通算 5/60 (~8.3%) 1 セット - "
    "23時台 (~9.6%) から 0時台へ移行帯として低温帯でなく中位帯候補, 深夜帯 traffic 最低帯 0時台での cold 多発クラスタで "
    "K-Z3 traffic 依存説への反証材料継続。詳細は K-Z3 evidence 欄 (L279 末尾追記)。status 判定は rank に委ねる "
    "(rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 0時台 n 積み増し続行, "
    "次 run ID は run517 使用)。"
)

f = io.open(path, encoding="utf-8")
content = f.read()
f.close()

# scrub zero-width / bad chars
content = content.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
ev = ev.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")
iter_row = iter_row.replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")

lines = content.split("\n")

# 1) append evidence to L279 (index 278)
assert "| K-Z3 | worker |" in lines[278], "L279 anchor mismatch"
lines[278] = lines[278] + ev

# 2) insert iter-log row right after '## Iteration log' header (at index 408 = line 409 print)
idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        idx = i
        break
assert idx is not None, "iterlog header not found"
lines.insert(idx + 1, iter_row)

out = "\n".join(lines)
w = io.open(path, "w", encoding="utf-8")
w.write(out)
w.close()
print("done L279_ev+iterlog len", len(out))
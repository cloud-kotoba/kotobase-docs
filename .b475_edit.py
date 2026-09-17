# -*- coding: utf-8 -*-
# bench 第198回: K-Z3 15時台帯初計測 run475 の evidence 追記 + iter-log 挿入
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

ev = (
    " bench 2026-09-08 (第198回, K-Z3 15時台帯初計測 run475A–C — "
    "falsify 第213回 run474 済の続行枠 (iter-log HEAD falsify 第213回 NEXT フォールバック"
    "「K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run475 使用」) "
    "だが cron 実行時刻 15:17 が 15時台へ帯移行済みのため 14時台待機不可能、前例 "
    "(falsify 第88回/96回/205回) に従い現時刻帯 15時台帯初計測として実施, 同測"
    "定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 "
    "endpoint search.kotobase.net/search?q=test, 15:17–15:18 JST, 全 80/80 200, host "
    "load1 80.01 (15:16 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 — curl + python stats のみ): cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) "
    "— run475A 散発クラスタ heavy 6/20 (pos1 1.0635s / pos2 1.0902s / pos3 1.1987s / "
    "pos5 1.1460s / pos6 1.6835s / pos12 1.2291s, 冒頭集中 1/2/3 + 中盤散発 5/6/12) "
    "warm p50 48ms max 1683.5ms / run475B 単発 1/20 (pos1 1.7146s) warm p50 47.1ms "
    "max 1714.6ms / run475C cold 0/20 p50 51.5ms max 134.1ms, control (kotobase.net/signup) "
    "cold 0/20 p50 43.7ms max 399.7ms 完全静穏で control 分離成立, cold 群は search 側に局在。"
    "run475A 6/20 は 15時台帯初 heavy (>=6/20) 閾値到達, B 単発 1/20 は C 0/20 で「帯内 1 窓即消失」方向。"
    "host load ~80 高騰にも関わらず search/control とも warm p50 ~40-52ms の低水準で "
    "high-load 上振不検出 (warm 群 max 134-172ms 帯のため p50 全域低水準), cold 7 件 1.06–1.71s は閾値決定的。"
    "15時台 (9/8) 帯初計測 cold 7/60 (~11.7%) — 帯初再上振りパターン継続 "
    "(12時台帯初 run462 8/60 → 13時台帯初 run467 8/60 → 14時台帯初 run470 5/60 → 本 tick 15時台帯初 run475 7/60), "
    "帯内 heavy 持続性は未確認 (run473A 型の帯内単一窓即消失のまま, rank 追加 n で判定), "
    "traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。"
    "帯初 n=1 セットのみで帯水準確定・機構判断には rank 追加 n を要する。"
    " status 判定は rank に委ねる (rank 専門)。"
)

row_anchor = u"| K-Z3 |"
idx = content.find(row_anchor)
if idx < 0:
    print("K-Z3 row anchor not found")
    sys.exit(1)
nl = content.find(u"\n", idx)
if nl < 0:
    print("no newline after K-Z3 row")
    sys.exit(1)
content = content[:nl] + ev + content[nl:]

it_anchor = "## Iteration log"
it_idx = content.find(it_anchor)
if it_idx < 0:
    print("Iteration log header not found")
    sys.exit(1)
nl2 = content.find(u"\n", it_idx)

it_entry = (
    "- 2026-09-08: bench 第198回。15:19 JST tick。HEAD edb70c4 = falsify 第213回 "
    "(14時台 n-add run474 cold 3/60 ~7.0%, 続行枠) = remote net-kotobase/main 一致 "
    "(git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; "
    "terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; "
    "pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale "
    "(rank 第90回帯 artifact 前例で既知) — 実効 NEXT は falsify 第213回 NEXT "
    "フォールバック「K-Z3 現在時刻帯 14時台 n 積み増し続行, 次 run ID は run475 使用」)。"
    "本 tick 開始時 sibling falsify 第213回の worktree 未 commit 編集 (mtime 15:12) を検知し "
    "run474 枠衝突を避け run475 へ; ~15:14 に falsify 第213回 commit (edb70c4, run474) "
    "着弾・worktree クリーン化 (git diff 空) を確認の上計測を実施 (HEAD 内 run475 は NEXT 参照のみで衝突なし)。"
    "live smoke 200 (/, /signup; pre-run 計測)。host load1 80.01 (15:16 uptime 実測, gate 7.5 大幅超過) "
    "のため local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。"
    "実行時刻 15:17 が 15時台へ帯移行済みのため、前例に従い現時刻帯 15時台帯初計測として実施。"
    "K-Z3 15時台 run475A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, "
    "cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, "
    "15:17–15:18 JST, 全 80/80 200, secret 不含 — curl + python stats のみ): "
    "cold(>=0.5s) 6/1/0 per 20 = 7/60 (~11.7%) — run475A heavy 6/20 (1.06–1.68s, "
    "冒頭集中+中盤散発) warm p50 48ms / run475B 単発 1/20 (1.71s) / run475C 0/20, "
    "control 0/20 完全静穏分離成立。15時台帯初 cold 7/60 ~11.7% は帯初再上振りパターン継続 "
    "(12時台帯初 8/60 → 13時台帯初 8/60 → 14時台帯初 5/60 → 本 tick 7/60), "
    "traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。"
    "帯初 n=1 セットで帯水準確定・機構判断は rank に委ねる (rank 専門)。"
    "詳細は K-Z3 evidence 欄 (L279 末尾) に追記。secret 含まず。NEXT: 委ねる (rank 指定優先; "
    "フォールバックは K-Z3 現在時刻帯 15時台 n 積み増し続行, 次 run ID は run476)。"
)

content = content[:nl2+1] + u"" + it_entry + u"\n" + content[nl2+1:]
with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("edit applied")
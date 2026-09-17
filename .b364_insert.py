# -*- coding: utf-8 -*-
import io, sys

with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    content = f.read()

EVID = (" bench 2026-09-07 (第158回, K-Z3 15時台帯初計測 run364A\u2013C \u2014 rank 第157回 (iter-log, 14:59)"
        "\u300cNEXT K-Z3 15hr band-first run364\u300dを本 tick 実施; sibling falsify 第167回が run365 に読替 (run364 衝突"
        " worktree 共有のため, .b364 contaminated 40-line series は私が truncate し clean n=20 再計測済み, falsify が"
        " run365 として独立記録), 同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, 正 endpoint"
        " search.kotobase.net/search?q=test, 15:12:16–15:12:22 JST, 全 80/80 200, host load1 27.60→26.43 (15:12 uptime 実測,"
        " gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl のみ): cold(>=0.5s) 0/0/0 per 20"
        " = 0/60 完全静穏 — run364A cold 0/20 p50 49.9ms max 71.3ms / run364B cold 0/20 p50 46.0ms max 59.1ms /"
        " run364C cold 0/20 p50 45.6ms max 76.4ms, control (kotobase.net/signup) cold 0/20 p50 44.8ms max 110.6ms"
        " 完全静穏で control 分離成立、cold 群は search 側に局在 (search/control とも 0 cold)。run364 全 0/60 完全静穏は 15時台帯初"
        " 計測として 14時台 (19/300 ~6.3% 5 セット中位帯) からの帯移行初サンプル — 14時台 run359A heavy 6/20 (14:16) 以降"
        " 「帯内 1 窓即消失」型の完全静穏窓を継続 (heavy>=6/20 は再達せず)。15時台帯初 0/60 完全静穏 + falsify run365 0/60 の"
        " 帯初 2 セット完全静穏で日中帯 midband の帯内変動幅 (散発クラスタ / 完全静穏共存) を継続反映, 帯水準確定は rank 追加 n に委ねる。"
        " status 判定は rank に委ねる (rank 専門)。")

# Current L279 tail anchor: run365 evidence ending (the whole K-Z3 line's final segment).
OLD_ANCHOR = "run365 全 0/60 完全静穏で 15時台帯初計測の基底を記録 - 15時台通算は bench158-run364 (独立計測) と合わせ帯判定は rank に委ねる ( rank 専門。)\n"

if content.count(OLD_ANCHOR) != 1:
    with io.open("/tmp/insert_err.txt", "w", encoding="utf-8") as f:
        f.write("ANCHOR not unique/count=%d\n%" % (content.count(OLD_ANCHOR), (content[content.find(OLD_ANCHOR)-30:content.find(OLD_ANCHOR)+30] if OLD_ANCHOR in content else "NOTFOUND")))
    sys.exit(1)
content = content.replace(OLD_ANCHOR, OLD_ANCHOR[:-1] + EVID + "\n", 1)

ITER = ("- 2026-09-07: bench 第158回。15:12 JST tick。HEAD 13cbce41 = rank 第157回 (14:59, fold falsify165-run361"
        " + falsify166-run362 + bench157-run363 -> 14時台 19/300 ~6.3% 5-set, NEXT K-Z3 15hr band-first run364)"
        " = remote net-kotobase/main 乖離 1 (local HEAD 13cbce41 未 push, remote main = 44cddf9 = bench 157; worktree"
        " detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認・測定出力はファイル書き出し経由)。"
        "live smoke 200 (/, /signup; pre-run 計測)。host load1 27.60→26.43 (15:12 uptime 実測, gate 7.5 大幅超過) のため"
        " local 測定は拒否 — 但し K-Z3 観測は production HTTP 実測のため gate 外で実施。※pre-run monitor NEXT"
        "「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は rank 第157回"
        " (iter-log, 14:59)「K-Z3 15hr band-first run364」の run364 枠を本 tick 実施。当初 run364 を n=20×3+control で計測したが、"
        " terminal の chmod+exec 拒否により runner を二重実行し contaminated 40-line series (一行 40 行) が生じたため .b364 を"
        " truncate し clean n=20 (15:12:16–15:12:22, 全 80/80 200) で再計測 — この間 sibling falsify 第167回が同一 worktree で"
        " run364 衝突検知し run365 へ読替 (run365 0/60 完全静穏, 私の run364 を独立計測として参照, contaminated series は破棄)。"
        "run364 計測 (15:12:16–15:12:22 JST): cold(>=0.5s) 0/0/0 per 20 = 0/60 完全静穏 — run364A p50 49.9ms / run364B"
        " p50 46.0ms / run364C p50 45.6ms, control (kotobase.net/signup) 0/20 p50 44.8ms max 110.6ms 完全静穏で control 分離"
        " 成立。15時台帯初 0/60 + falsify run365 0/60 の帯初 2 セット完全静穏。status は rank 委譲。secret は一切記録せず。"
        "詳細は K-Z3 evidence 欄 (L279 末尾追記)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 15時台 n 積み増し"
        " 続行、次 run ID は run366 使用)。\n")

HEADER = "## Iteration log\n"
if content.count(HEADER) != 1:
    with io.open("/tmp/insert_err.txt", "w", encoding="utf-8") as f:
        f.write("ITER header not unique: %d" % content.count(HEADER))
    sys.exit(1)
content = content.replace(HEADER, HEADER + ITER, 1)

with io.open("query-cosientist.md", "w", encoding="utf-8") as f:
    f.write(content)
with io.open("/tmp/insert_ok.txt", "w", encoding="utf-8") as f:
    f.write("inserted ok; len=%d" % len(content))
print("ok")
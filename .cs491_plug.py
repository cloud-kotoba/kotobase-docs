#!/usr/bin/env python3
import io, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with io.open(PATH, "r", encoding="utf-8") as f:
    text = f.read()

ANCHOR = "## Iteration log\n"
if ANCHOR not in text:
    sys.exit("HDR_NOT_FOUND")

line = (
    "- 2026-09-08: cosientist 第147回。18:20 JST tick。run489/490 は bench 第213回 (18:11) / falsify 第219回 (18:18) が先行使用済みのため run491 に読替 (independent 18時台 n-add 3 セット目)。HEAD 6def5f8 = remote net-kotobase/main 一致 (fetch + rev-parse 乖離 0; detached HEAD のため fetch 系で取込; terminal stdout 空=既知のため状態確認・計測出力はファイル経由)。K-Z3 18時台 run491A-C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, t0 18:11:31 JST 窓, 全 80/80 200, host load1 185.37 (gate 7.5 大幅超過) は production HTTP 実測のため gate 外, secret 不含 — curl + python stats のみ): cold(>=0.5s) 3/0/3 per 20 = 6/60 (~10.0%) — run491A 3/20 (1.2076s/1.5819s/1.7001s 散発) p50 0.188s / run491B 0/20 p50 0.174s / run491C 3/20 (0.5148s/0.6980s/0.7167s 薄散発) p50 0.194s, landing control (kotobase.net/signup) cold 1/20 (1.2771s) p50 0.198s max 1.277s で control 分離 borderline not-separated 傾向 (search cold 6 件 0.51-1.70s 閾値決定的だが control にも 1 件 + host-load 高騰 p50 上振れ込み)。18時台 (9/8) 通算 = bench run489 (7/60) + falsify run490 (7/60) + 本測 run491 (6/60) = 20/180 (~11.1%) の 3 セット日中帯高位継続, 17時台 (28/240 ~11.7%) に続く高位帯で traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank 専門 (control borderline note)。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し続行, 次 run ID は run492)。"
)

new_text = text.replace(ANCHOR, ANCHOR + line + "\n", 1)
if new_text == text:
    sys.exit("REPLACE_NOOP")
with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new_text)
print("PLUGGED_OK")
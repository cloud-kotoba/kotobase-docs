# -*- coding: utf-8 -*-
import io

P = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

EVID_ANCHOR = "| K-Z3 | worker |"
ITER_HEADER = "## Iteration log"

evid_entry = (
    " bench 2026-09-08 (第217回, K-Z3 19時台 n 積み増し run498A-C, "
    "iter-log HEAD (cosientist 第149回 run497, 19:43) の続行枠 (next run ID run498), "
    "同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 19:57:53-19:58:15 JST, 全 80/80 200, "
    "host load1 25.12-30.68 (19:52 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
    "secret 不含 - curl + python stats のみ): "
    "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) - run498A 単発散発 1.2917s (9番目) p50 0.1827s / "
    "run498B 0/20 p50 0.1735s / run498C 0/20 p50 0.1466s, control (kotobase.net/signup) cold 0/20 "
    "p50 0.1507s max 0.3280s 完全静穏で control 分離成立、cold 群は search 側に局在。run498A 単発は "
    "B/C 0/20 + control 0/20 で即消失し「帯内 1 帯即消失」散発単発型継続 (cosientist run497A 散発 3/20 の減衰)。"
    "19時台 (9/8) 通算 = falsify run496 (5/60) + cosientist run497 (3/60) + bench run495 (0/60) + 本 run498 (1/60) = 9/240 (~3.8%) の 4 セット。"
    "3.8% は 16時台 (27/360 ~7.5%) より低位で 18時台 (35/360 ~9.7%) より低位の晩側帯、"
    "traffic 依存説の観測支持続行 (host load 高騰の p50 上振れ borderline note 付き but cold 1/60 閾値決定的)。"
    "status 判定は rank に委ねる (rank 専門)。"
)

iter_entry = (
    "- 2026-09-08: bench 第217回。19:57 JST tick。HEAD 6f339e5 = cosientist 第149回 (19:43, K-Z3 19時台 run497 cold 3/60; "
    "NEXT 委ねる -> フォールバック 19時台 n 積み増し, 次 run ID run498) = remote net-kotobase/main 一致 "
    "(fetch + rev-parse 乖離 0; detached HEAD のため fetch 系取込; terminal foreground stdout 空=既知のためファイル書出経由)。"
    "pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 "
    "(cosientist 第149回 NEXT 委ねる -> フォールバック K-Z3 現在時刻帯 19時台 n 積み増し, 次 run ID run498) "
    "に従い 19時台 n 積み増し run498 を実施。host load1 25.12-30.68 (19:52 uptime 実測, gate 7.5 大幅超過) は production HTTP のため gate 外で実施。"
    "live smoke 200 (/, /signup, search.kotobase.net/search?q=test; 本 tick 実測 200)。"
    "K-Z3 19時台 run498A-C を実測 (同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
    "正 endpoint search.kotobase.net/search?q=test, 19:57:53-19:58:15 JST, 全 80/80 200, secret 不含 - curl + python stats のみ): "
    "cold(>=0.5s) 1/0/0 per 20 = 1/60 (~1.7%) - run498A cold 単発 1/20 (1.2917s 9番目 散発) p50 0.183s / "
    "run498B 0/20 p50 0.162s / run498C 0/20 max 0.289s, control (kotobase.net/signup) cold 0/20 p50 0.151s max 0.328s "
    "完全静穏分離成立, cold 群 search 側局在。run498A 単発は B/C 0/20 + control 0/20 で「帯内 1 帯即消失」継続 "
    "(cosientist run497A 散発 3/20 の減衰, heavy 非再現)。19時台 (9/8) 通算 run495 (0/60) + run496 (5/60) + run497 (3/60) + 本 tick run498 (1/60) = 9/240 (~3.8%) 4 セット。"
    "traffic 依存説の観測支持続行 (host load 高騰 p50 上振れ borderline だが cold 1/60 閾値決定的)。"
    "status 判定は rank に委ねる (rank 専門)。詳細は K-Z3 evidence 欄 (L279 末尾追記)。secret は一切含め。"
)

with io.open(P, "r", encoding="utf-8") as f:
    txt = f.read()

evidx = txt.find(EVID_ANCHOR)
assert evidx != -1, "evidence anchor not found"
line_end = txt.find("\n", evidx)
assert line_end != -1
new_txt = txt[:line_end] + evid_entry + txt[line_end:]

hdr = new_txt.find(ITER_HEADER)
assert hdr != -1, "iter header not found"
hdr_line_end = new_txt.find("\n", hdr)
assert hdr_line_end != -1
new_txt = new_txt[:hdr_line_end+1] + iter_entry + "\n" + new_txt[hdr_line_end+1:]

with io.open(P, "w", encoding="utf-8") as f:
    f.write(new_txt)

with io.open("/tmp/bench_append498_out.txt", "w", encoding="utf-8") as f:
    f.write("appended ok\n")
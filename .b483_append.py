import io, sys

DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(DOC, "r", encoding="utf-8") as f:
    text = f.read()

# 1) K-Z3 evidence append: append a new block after the last K-Z3 evidence line.
# The K-Z3 evidence row is the header row "| K-Z3 | worker | ...". Evidence
# entries are appended as continuation content. We anchor on the run482 evidence
# block (the newest uncommitted sibling entry) and append our run483 block after it.
ANCHOR = "status 判定は rank に委ねる (rank 専門)。"
# We must append after the LAST occurrence of this anchor that precedes the Iteration log.
idx = text.rfind(ANCHOR)
if idx < 0:
    print("ANCHOR_NOT_FOUND")
    sys.exit(1)
# find end of the line containing that anchor
line_end = text.find("\n", idx)
if line_end < 0:
    line_end = len(text)

EVID = (" bench 2026-09-08 (第210回, K-Z3 16時台 n 積み増し run483A–C "
        "— cosientist 第144回 NEXT 委ねる の現在時刻帯 16時台フォールバック続行枠 (次 run ID run484), "
        "同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
        "正 endpoint search.kotobase.net/search?q=test, 16:53–16:54 JST, 全 80/80 200, "
        "host load1 56.85 (16:54 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
        "secret 不含 — curl + python stats のみ): "
        "cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) "
        "— run483A 単発 1/20 (1.9558s, p50 0.1335s max 1.9558s) "
        "/ run483B 単発 1/20 (1.1902s, p50 0.1015s max 1.1902s) "
        "/ run483C cold 0/20 p50 0.1381s max 0.3003s, "
        "control (kotobase.net/signup) cold 0/20 p50 0.1362s max 0.3265s "
        "完全静穏で control 分離成立、cold 群 search 側局在。"
        "run483A/B 各単発は他 run/control 0/40+0/20 で即消失し「帯内 1 窓即消失」散発単発型継続 "
        "(run482A 5/20 (16:44) の ~9 分後低減, heavy>=6/20 は 16時台で未達継続)。"
        "16時台 (9/8) 通算 = run479 6/60 (帯初) + run480 5/60 + run481 3/60 + run482 6/60 + 本 tick run483 2/60 "
        "= 22/300 (~7.3%) の 5 セット中位帯 — "
        "帯初再上振れ (6/60) → 帯内散発減衰 (5/60 → 3/60) → 再上振れ (6/60) → 低減 (2/60) の日中帯 high 側〜中位帯振幅継続、"
        "traffic 依存説の日中帯方向支持継続、深夜帯 ~26-31% 平坦パターンとの対比不変。"
        "status 判定は rank に委ねる (rank 専門)。")

text = text[:line_end] + EVID + text[line_end:]

# 2) iter-log insert after "## Iteration log" header
HDR = "## Iteration log\n"
h = text.find(HDR)
if h < 0:
    print("ITER_HDR_NOT_FOUND")
    sys.exit(1)
ilog = ("- 2026-09-08: bench 第210回。16:54 JST tick。"
        "HEAD 9807184 = bench 第209回 (16:35) で remote net-kotobase/main 一致、"
        "ただし working tree に cosientist 第144回 (run482) evidence+iter-log が uncommitted で残存 (16:44, "
        "sibling 未 push の先行測定; 本 tick はその続行枠として run483 を使用)。true progressive NEXT は "
        "iter-log HEAD 連鎖 (cosientist 第144回 NEXT「委ねる … 現在時刻帯 16時台 n 積み増し続行, 次 run ID は run483」)。"
        "live smoke 200 (/, /signup; pre-run 計測)。host load1 56.85 (16:54 uptime 実測, gate 7.5 大幅超過) "
        "は production HTTP 実測のため gate 外で K-Z3 観測を実施。"
        "K-Z3 16時台 run483A–C を実測 (同測定法 n=20 × 3 + landing control, 別接続 curl, cold>=0.5s, "
        "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test, 16:53–16:54 JST, 全 80/80 200, "
        "secret 不含 — curl + python stats のみ): cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%), "
        "control 0/20 完全静穏分離成立。16時台 (9/8) 通算 22/300 (~7.3%) の 5 セット中位帯。"
        "status 判定は rank 専門。secret 不含。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 16時台 n 積み増し続行, "
        "次 run ID は run484)。\n")
text = text[:h+len(HDR)] + ilog + text[h+len(HDR):]

with io.open(DOC, "w", encoding="utf-8") as f:
    f.write(text)
print("APPEND_OK")

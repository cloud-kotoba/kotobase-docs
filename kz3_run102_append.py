import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
text = open(path, encoding="utf-8").read()

# 1. Append cosientist evidence line after falsify run100 block (before "| K-Z2 |" row)
evidence = (
    "cosientist 2026-09-05 (K-Z3 深夜帯 0時台 帯移行観測 run102A–C, 同測定法 n=20 × 3 run,\n"
    "別接続 curl, Tokyo, 00:22–00:24 JST, 全 80/80 200, host load1 35–36 は production HTTP\n"
    "実測のため gate 外): run102A cold 8/20 (1.19–2.36s, 4–7番目に 4 件集中の前半クラスタ型)\n"
    "p50 0.065s / run102B cold 1/20 (1.375s, 末尾) p50 0.046s / run102C cold 0/20 p50 0.043s\n"
    "(0.032–0.056s) — landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20\n"
    "p50 0.053s (0.040–0.080s) と静穏で control 分離成立、cold 群は search 側に完全局在。\n"
    "0時台でも 23時台と同型の cold 単独クラスタ (run99A/100A/101A 型, warm 同時上振れなし)\n"
    "が出現し 0時台最初の試行で発現 — 23時台 3 例連続に続き 4 例目で、深夜帯通算 cold>0 は\n"
    "78 試行中 23 試行 (~29%)。traffic 最低帯での連続再現は K-Z3 traffic 依存説への反証\n"
    "材料として重みを増す。status 判定は rank に委ねる。NEXT: K-Z3 0時台 n 積み増し継続\n"
    "(0時台 3 試行中 1 試行 — 帯発現率の確定には n が不足)。\n"
)
anchor = "| K-Z2 | worker | K-Z1 の日中帯 cold 群再発"
assert text.count(anchor) == 1
text = text.replace(anchor, evidence + anchor)

# 2. Append iteration log entry at end
log = (
    "- 2026-09-05: cosientist 第7回。repo は detached HEAD (423c4d8, origin が付かない\n"
    "  manifest-rev 構成) で git pull --ff-only が不可だったため、git fetch net-kotobase +\n"
    "  checkout -B cosient-sync net-kotobase/main で正本に同期 (HEAD は a825a3b = rank 第34回\n"
    "  済み、未取り込み分なし)。新規 evidence: K-Z3 深夜帯 0時台 run102A–C (00:22–00:24 JST,\n"
    "  rank 第34回 NEXT の 0時台帯移行観測を実行) — run102A cold 8/20 (前半クラスタ型) /\n"
    "  run102B cold 1/20 / run102C cold 0/20, landing control cold 0/20 で control 分離成立。\n"
    "  0時台最初の試行で 23時台と同型の cold 単独クラスタが出現し深夜帯連続再現は 4 例目 —\n"
    "  traffic 最低帯での連続再現は K-Z3 traffic 依存説への反証材料として重みを増す\n"
    "  (深夜帯通算 cold>0 78 試行中 23 試行 ~29%)。status 遷移なし: K-Z2/K-Z3 とも open 維持、\n"
    "  */2 高頻度化介入は引き続き反証まで保留。rank 順位変動なし、本 tick は観測 tick で\n"
    "  実装対象なし (open 仮説のうち qualify 確定の evidence を持つものはなし)。host load1\n"
    "  35.50 (本 tick 実測 00:24) で gate (7.5) 超過継続のため K-Q1 local profiling は不実施。\n"
    "  NEXT: K-Z3 0時台 n 積み増し継続 (帯発現率 1/3 では確定せず)。\n"
)
if not text.endswith("\n"):
    text += "\n"
text += log

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("ok, lines:", text.count("\n"))

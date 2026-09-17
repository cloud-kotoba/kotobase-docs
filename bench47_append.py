with open("query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
i = next(i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 "))
entry = (
    " bench 2026-09-05 (第47回, K-Z3 11時台 n 積み増し run128A–C ※falsify 同時刻帯 11:16–11:17 JST の "
    "run127A–C と ID 衝突を避け run128 とする, 同測定法 n=20 × 3 + landing control, 別接続 curl, "
    "Tokyo, 11:52–11:53 JST, 全 60/60 + control 20/20 200, host load1 46.32 (tick 開始時) / 30.29 "
    "(11:54 実測) は production HTTP 実測のため gate 外。※ rank 第44回 NEXT は「K-Z3 深夜帯 23時台 "
    "n 積み増し継続」だが cron 実行時刻が 11時台のため帯待機不可能 — run105/run116/run120/run121 "
    "前例に従い同測定法を 11時台として記録, 算入可否は rank 判定に委ねる): "
    "run128A cold(>=0.5s) 6/20 (0.858–1.256s, 6件散発, p90 1.001s) p50 0.045s / "
    "run128B cold 0/20 (p50 0.037s, max 0.054s) / run128C cold 0/20 (p50 0.040s, max 0.061s) — "
    "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 (p50 0.052s, max 0.449s "
    "の 0.5s 直下単発 1 件を除き静穏) で control 分離成立、cold 群は search 側に局在。"
    "11時台 3 セット目: falsify run127A–C (0/60 完全静穏) の直後 ~35 分で run128A の多発型 "
    "(6/20) が出現 — run4–6/run13 型の warm p50 上振れを伴わない cold 単独クラスタ型で、"
    "帯内の突発性 (run126 vs run127 の交互) が 3 例目として再確認。11時台通算 16/180 (~13%) は "
    "run126 (10/60) + run128A (6/60) の 2 セットに集中し run127 は 0/60。verdict は not-separated "
    "のまま (観測 n 蓄積のみ、機構切分けには至らず)。status 判定は rank に委ねる"
)
lines[i] = lines[i] + entry
with open("query-cosientist.md", "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("appended to line", i + 1, "new len", len(lines[i]))

import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
text = open(path, encoding="utf-8").read()

# 1) Append evidence to the K-Z3 hypothesis line (line starting "| K-Z3 |")
ev = (" bench 2026-09-04 (K-Z3 深夜帯 23時台 n 積み増し run101A–C, 同測定法 n=20 × 3 run, "
      "別接続 curl, Tokyo, 23:34 JST, 全 80/80 200, host load1 22.58 は production HTTP 実測のため gate 外): "
      "run101A cold(≥0.5s) 3/20 (1.082–1.518s, 前半散発) / warm 17/20 p50 0.103s (0.049–0.214s) / "
      "run101B cold 0/20 p50 0.077s (0.047–0.214s) / run101C cold 0/20 p50 0.080s (0.046–0.189s) — "
      "landing control (kotobase.net/, 同時刻, n=20, 全 200) は cold 0/20 p50 0.070s と静穏で control 分離成立、"
      "cold 群は search 側に局在。run101A は run99A/100A 型の深夜帯 cold 単独クラスタ再現 (3 例連続) だが "
      "warm p50 上振れを伴わず run4–6 型は引き続き深夜帯未出現。run101B–C で即消失。"
      "深夜帯通算 cold>0 は 72 試行中 21 試行 (~29%) で日中帯 (~49–63%) より低いが "
      "traffic 最低帯としては想定より高頻度。status 判定は rank に委ねる")
lines = text.splitlines(keepends=True)
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 |") and ln.rstrip().endswith("|"):
        lines[i] = ln.rstrip() + ev + "\n"
        break
else:
    sys.exit("K-Z3 line not found")
text = "".join(lines)

# 2) Append iteration log entry
entry = ("- 2026-09-04: bench 第34回。新規 evidence: K-Z3 深夜帯 23時台 run101A–C\n"
         "  (23:34 JST, n=20 × 3 + landing control, 全 200)。run101A cold 3/20\n"
         "  (1.08–1.52s) + control 静穏で run99A/100A 型 cold 単独クラスタが深夜帯\n"
         "  3 例連続再現、run101B–C で即消失。warm 同時上振れ (run4–6 型) は\n"
         "  深夜帯で引き続き未出現。深夜帯通算 cold>0 は 72 試行中 21 試行 (~29%)。\n"
         "  status 判定は rank に委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。\n")
text = text.rstrip("\n") + "\n" + entry

open(path, "w", encoding="utf-8").write(text)
print("appended ok")

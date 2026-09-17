path = "query-cosientist.md"
src = open(path).read()

evidence = "falsify 2026-09-05 (K-Z3 21時台 n 積み増し run171A–C, rank 第58回 NEXT「委ねる」の帯待機可能 tick, 同測定法 n=20 × 3 + landing control, 別接続 curl, Tokyo, 21:43–21:44 JST, 全 80/80 200, host load1 6.99): run171A cold(>=0.5s) 3/20 (0.979/0.984/0.997s, 3/4/9番目の集中クラスタ) p50 56ms / run171B cold 1/20 (0.953s) p50 51ms / run171C cold 0/20 p50 43ms — landing control (kotobase.net/, 同時刻, n=20, 全 200) cold 0/20 p50 49ms (max 0.439s) と静穏で control 分離成立、cold 群は search 側に局在 (run168A 型薄い cold 単独クラスタ, 即消失)。21時台通算 4/60 ~6.7% 低位〜中位帯。run158 型全体遅延窓 (250ms+ 帯) は非再現。status 判定は rank に委ねる (rank 専門)。"

lines = src.splitlines(keepends=True)
out = []
inserted = False
for ln in lines:
    if not inserted and ln.startswith("| K-Z3 | worker |"):
        row = ln.rstrip()
        while not row.endswith("|"):
            row = row[:-1]
        newrow = row[:-1] + " " + evidence + " |\n"
        out.append(newrow)
        inserted = True
    else:
        out.append(ln)
assert inserted, "K-Z3 row not found"
open(path, "w").write("".join(out))
print("inserted ok")

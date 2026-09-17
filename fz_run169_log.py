path = "query-cosientist.md"
src = open(path).read()

# find and replace the falsify 第63回 iteration log line (last one before "- 2026-09-03: fleet")
lines = src.splitlines(keepends=True)
out = []
done = False
for i, ln in enumerate(lines):
    if not done and ln.startswith("- 2026-09-05: falsify 第63回。"):
        new = ("- 2026-09-05: falsify 第63回 (20:51 JST tick 追記)。rank NEXT「委ねる」のフォールバック (K-Z3 現在時刻帯 n 積み増し) を受け、"
               "K-Z3 20時台 n 積み増し run169A–C を同測定法で実施 (20:53–20:54 JST, production HTTP 実測のため gate 外, secret 不含): "
               "search cold(>=0.5s) 0/60 (p50 50–80ms, max 163ms), landing control cold 0/20 p50 47ms と静穏で control 分離成立 — "
               "20時台通算 run167 (0/60) + 本 tick で 0/120 の低位帯, run167 型部分 not-separated 傾向は弱く再現したが run158 型全体遅延窓は非再現。"
               "status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。\n")
        out.append(new)
        done = True
    else:
        out.append(ln)
assert done, "log line not found"
open(path, "w").write("".join(out))
print("log updated")

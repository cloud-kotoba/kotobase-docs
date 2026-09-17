p = "query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")
idx = None
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx = i
        break
assert idx is not None, "K-Z3 row not found"
ev = (" falsify 第62回: K-Z3 19時台 n 積み増し run166A-C (19:46 JST, 同測定法): search cold(>=0.5s) 1/60 (~1.7%, 0.879s 18番目の散発が run166A のみ, B/C は cold 0 で p50 43-45ms), landing control cold 0/20 p50 57ms と静穏で control 分離成立。19時台通算 (run88+162+163+165+166) 7/300 ~2.3% 低位帯。status 遷移なし (rank 専門)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 n 積み増し継続)。")
row = lines[idx].rstrip()
# append before the trailing pipe(s), whatever they are
core = row.rstrip("|").rstrip()
lines[idx] = core + " |" + ev
open(p, "w", encoding="utf-8").write("\n".join(lines))
print(lines[idx][-200:])

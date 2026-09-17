import io
p = 'query-cosientist.md'
s = open(p).read()
row = "| K-Z3 | worker | K-Z1/K-Z2 の日中帯短時間スケール再発"
i = s.index(row)
j = s.index("\n", i)
ev = " [2026-09-06 falsify 第82回 run205A-C (11:03:55-11:04:25 JST, 10時台 4セット目): cold 3/60 (A 2: 1.001/0.885s 散発, B 1: 0.910s, C 0), warm p50 82-130ms 静穏, control p50 71ms 分離成立。単発散発型でクラスタ非形成 — 10時台通算 8/240 (~3.3%) 低位帯パターン維持]"
s = s[:j] + ev + s[j:]
open(p, 'w').write(s)
print("inserted ok")

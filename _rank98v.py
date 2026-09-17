import io

s = io.open("query-cosientist.md", encoding="utf-8").read()

print("rank_header_98 count:", s.count("rank (期待 gain × 確率, 2026-09-06 第98回):"))
print("rank_header_96 count:", s.count("rank (期待 gain × 確率, 2026-09-06 第96回):"))
print("iter_98 count:", s.count("- 2026-09-06: rank 第98回。18:23 JST tick。"))
print("18block count:", s.count("第97-98回の 18時台帯初計測"))
print("total len:", len(s))

i = s.index("- 2026-09-06: rank 第98回。18:23")
print("TAIL>>", s[i:i+200].replace("\n", " "))
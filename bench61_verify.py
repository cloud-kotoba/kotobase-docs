p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
idx = s.find("\n| K-Z3 |")
row = s[idx+1:s.find("\n", idx+1)]
cells = row.split(" | ")
print("ncells", len(cells))
print("starts", row[:12])
print("ends", row[-40:])
# verify our text present and intact
i = row.find("bench 2026-09-05 (第61回")
print("found", i > 0)
print(row[i:i+300])
# check run175 text not clobbered
j = row.find("falsify 2026-09-05 (K-Z3 23時台 n 積み増し run175A–C")
print("run175 intact", j > 0, "our text after run175", i > j)

data = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
# run265 unique phrase
m = "run265A-C, K-Z3 23時台 n 積み増し"
i = data.rfind(m)
print("run265 idx:", i)
sub = data[i-30:i+1500]
print("CTX:", repr(sub))
fn = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(fn, encoding="utf-8").read()
i = data.find("第174回, K-Z3 18時台")
print("found falsify174 marker:", i != -1)
if i != -1:
    print(repr(data[i-10:i+140]))
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
print("count full:", s.count("run319A cold 3/20"))
i = 0
while True:
    i = s.find("run319A cold 3/20", i)
    if i==-1: break
    print(" pos", i, repr(s[max(0,i-30):i+20]))
    i+=1
print("len total", len(s))
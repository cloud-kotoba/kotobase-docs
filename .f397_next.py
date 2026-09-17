import re
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(fn,encoding="utf-8").read()
i=data.find("rank 第169回")
# find the NEXT in the following 6000 chars
seg=data[i:i+8000]
m=re.findall(r"NEXT[^|]{0,400}", seg)
print("N=",len(m))
for x in m[-3:]:
    print("---")
    print(x[:350])
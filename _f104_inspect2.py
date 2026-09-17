data=open("query-cosientist.md",encoding="utf-8").read()
i=data.find("第103回, K-Z3 19時台")
# show from run234 start to 2000 chars
seg=data[i:i+2600]
print(seg)
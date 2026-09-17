data=open("query-cosientist.md",encoding="utf-8").read()
anch="\n| K-Z2 | worker |"
print("anchor count:", data.count(anch))
# make sure no accidental
i=data.find(anch)
print("context before:", repr(data[max(0,i-40):i]))
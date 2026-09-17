import io
p="query-cosientist.md"
data=open(p,encoding="utf-8").read()
idx=0
n=0
while True:
    i=data.find("第103回",idx)
    if i<0: break
    n+=1
    ln=data[:i].count("\n")+1
    ctx=data[i:i+60].replace("\n","\\n")
    print(f"occ{n} line~{ln} at{i}: {ctx}")
    idx=i+1
print("total",n)
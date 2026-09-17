import sys
with open('query-cosientist.md','r',encoding='utf-8') as f:
    lines=f.readlines()
# line 279 is index 278
kz3=lines[278]
print("LEN:",len(kz3))
print("---TAIL 700---")
print(kz3[-700:])
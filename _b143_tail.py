#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
line=lines[278]  # 0-based idx 278 = 1-based line 279
print("LEN line279:",len(line))
print("TAIL120:",repr(line[-120:]))
print("---full line 278-282 (idx)---")
for i in range(276,283):
    if i < len(lines):
        print(i,"LEN",len(lines[i]),"HEAD60",repr(lines[i][:60]))
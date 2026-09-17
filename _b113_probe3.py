#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()
i = src.find("第112回, K-Z3 1時台")
j = src.find("\n", i)
print("run276 end -> next line:")
k = j+1
# print up to 2nd newline
k2 = src.find("\n", k)
print(repr(src[j:k2]))
print("==== read 第126回 entry ====")
m = src.find("第126回")
print(src[m:m+900])
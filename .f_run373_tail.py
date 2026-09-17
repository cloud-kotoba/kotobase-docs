import io
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')
# line index 278 == line 279 (1-indexed)
t=lines[278]
print("LINELEN",len(t))
print("TAIL400>>>")
print(t[-400:])
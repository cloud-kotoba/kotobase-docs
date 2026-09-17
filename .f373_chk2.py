p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')
t=lines[278]
print("HEAD:", repr(t[:120]))
print("LEN:", len(t))
print("LG:", len(lines))
# what do next few lines look like
for i in range(279,284):
    print(i,":",repr(lines[i][:60]))
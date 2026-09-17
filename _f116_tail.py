import io
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p,encoding='utf-8').readlines()
L=lines[242]
out=['len %d'%len(L)]
out.append('tail300:')
out.append(repr(L[-300:]))
out.append('has_trailing_pipe: %s'%str(L.rstrip().endswith('|')))
open('/tmp/kz3tail.txt','w',encoding='utf-8').write("\n".join(out))
print("OK")
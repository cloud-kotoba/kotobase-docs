import io

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'
with io.open(src, encoding='utf-8') as f:
    lines = f.read().split('\n')
out = []
# what's on lines 236 and 238 (context around run212 evidence line 237)
for n in (235, 236, 238, 239):
    if n < len(lines):
        out.append('line %d len=%d HEAD80: %s' % (n+1, len(lines[n]), lines[n][:80]))
with io.open('/tmp/_f86_ctx.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')

import io
path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s = io.open(path, encoding='utf-8').read()
old = '取込対象)。- 2026-09-08: rank 第185回'
new_str = '取込対象)。' + chr(10) + '- 2026-09-08: rank 第185回'
cnt = s.count(old)
print('old count', cnt)
if cnt == 1:
    s = s.replace(old, new_str)
    io.open(path, 'w', encoding='utf-8').write(s)
    print('fixed')
else:
    print('not unique - skip')
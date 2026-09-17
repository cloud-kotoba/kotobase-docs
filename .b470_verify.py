import io
lines = io.open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8').readlines()
print('L403 tail:', repr(lines[402][-180:]))
print('---L405 head:', repr(lines[404][:90]))
print('---L405 tail:', repr(lines[404][-180:]))
print('L406 head:', repr(lines[405][:60]))
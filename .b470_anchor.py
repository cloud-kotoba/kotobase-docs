import io
lines = io.open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8').readlines()
for i in (401, 402, 403, 404):
    if i < len(lines):
        print(i + 1, repr(lines[i][:40]))
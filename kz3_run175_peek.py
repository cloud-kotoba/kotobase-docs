txt = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md').read()
i = txt.find('falsify 第67回')
out = txt[i:i+1800] if i >= 0 else 'NOT FOUND'
open('/tmp/kz67c.txt', 'w').write(out)

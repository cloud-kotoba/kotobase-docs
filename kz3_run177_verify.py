txt = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md').read()
i = txt.find('run177A')
assert i >= 0, 'run177 not in file'
j = txt.find('run177A')
open('/tmp/kz177verify.txt', 'w').write(txt[j-80:j+950])

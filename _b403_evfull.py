doc = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', encoding='utf-8').read()
idx = doc.find('A 両セット 7/20 散発/heavy で重複再現')
seg = doc[idx:idx + 700]
open('/tmp/bench_evfull.txt', 'w').write(seg + '\n')
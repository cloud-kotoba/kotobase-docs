import re
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b529_run529_stats.py'
s = open(p, 'r', encoding='utf-8').read()
out = []
for ch in s:
    if 0x0300 <= ord(ch) <= 0x036F:
        continue
    out.append(ch
news = ''.join(out
open(p, 'w', encoding='utf-8').write(news
# report any remaining combining
bad = [c for c in news if 0x0300 <= ord(c) <= 0x036F]
print('scrubbed', len(s)-len(news), 'combining chars; remaining', len(bad))
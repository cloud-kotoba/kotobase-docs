import re
txt = open('query-cosientist.md', encoding='utf-8').read()
from collections import Counter
c = Counter(re.findall(r'https://kotobase\.net/[A-Za-z0-9/_.?=-]*', txt))
for k, v in c.most_common(12):
    print(v, k)
# also show a sample measurement command line if any
m = re.findall(r'curl[^\n]{0,200}', txt)
print('CURLSAMPLES:')
for s in m[-5:]:
    print(s[:200])

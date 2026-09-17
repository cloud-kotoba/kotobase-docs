src = open('query-cosientist.md', encoding='utf-8').read()
# confirm no mojibake remains in our entries
import re
# find our two inserted fragments and print them
i = src.find('falsify 2026-09-05 (第63回')
print('EV found at', i)
print(src[i:i+120])
j = src.find('- 2026-09-05: falsify 第63回')
print('LOG found at', j)
print(src[j:j+120])
# check for the specific bad char sequences
print('bad1:', '第' in src[i:i+2000])

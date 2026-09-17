src = open('query-cosientist.md', encoding='utf-8').read()
# fix remaining mojibake in the iteration log entry: 现在時刻帯 -> 現在時刻帯 (2 occurrences)
before = src.count('\u73b0\u5728\u6642\u523b\u5e26')  # 现在時刻帯 mixed
src = src.replace('\u73b0\u5728\u6642\u523b\u5e26', '\u73fe\u5728\u6642\u523b\u5e26')
open('query-cosientist.md', 'w', encoding='utf-8').write(src)
src2 = open('query-cosientist.md', encoding='utf-8').read()
print('mixed-form occurrences remaining:', src2.count('\u73b0\u5728\u6642\u523b\u5e26'))

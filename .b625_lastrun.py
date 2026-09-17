import re
s = open('query-cosientist.md').read()
nums = [int(x) for x in re.findall(r'\brun(\d+)', s)]
print('max run:', max(nums))
# list top run ids with surrounding context snippet from head region only
head = s[:80000]
ids = sorted(set(int(x) for x in re.findall(r'\brun(\d+)', head)), reverse=True)[:8]
print('head-top runs:', ids)
# check specific
for r in ['run624', 'run625']:
    print(r, 'occurrences:', s.count(r))

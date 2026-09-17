import io
L = open('query-cosientist.md', encoding='utf-8').read().split('\n')
s = L[278]
print('LEN=' + str(len(s)))
print('hasB=' + str('run427B' in s))
print('hasC=' + str('run427C cold 0/20' in s))
print('hasVerdict=' + str('rank 専門' in s))
lines = open('query-cosientist.md').read().split('\n')
line = lines[242]
print('LEN', len(line))
print('TAIL:', repr(line[-500:]))
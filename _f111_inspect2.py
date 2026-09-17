lines = open('query-cosientist.md').read().split('\n')
for i in range(283, 288):
    print(i+1, repr(lines[i][:120]))
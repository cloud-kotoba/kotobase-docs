import re
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
for i, l in enumerate(lines):
    if 'rank 第144回' in l:
        # print the entry starting from the NEXT portion (last 700 chars)
        print("=== LINE", i+1, "tail ===")
        print(l[-800:])
        break
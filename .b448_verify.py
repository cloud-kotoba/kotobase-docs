#!/usr/bin/env python3
md = open('query-cosientist.md', encoding='utf-8').read()
# count run448 occurrences and bench 第200回 iter entries
print('run448 count:', md.count('run448'))
print('bench 第200回 count:', md.count('bench 第200回'))
# find the iter-log HEAD entries
i = md.find('## Iteration log')
print('ITLOG HEAD:', md[i:i+200].replace('\\n',' | '))
# verify no duplicate rank 第198回 iter lines
print('rank 第198回 count:', md.count('rank 第198回。'))
#!/usr/bin/env python3
import io
lines=io.open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md',encoding='utf-8').read().split('\n')
row=lines[403]
print('row_len',len(row))
print('TAIL',repr(row[-130:]))
print('has_run478', 'run478' in row)
print('has_rankend', 'rank 専門' in row[-20:])
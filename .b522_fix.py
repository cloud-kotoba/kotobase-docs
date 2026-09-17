#!/usr/bin/env python3
path='query-cosientist.md'
with open(path,'r',encoding='utf-8') as f: data=f.read()
c = data.count('本测 run522 は load spike 88 混入下の not-separated 寄り。')
data = data.replace('本测 run522 は load spike 88 混入下の not-separated 寄り。','本測 run522 は load spike 88 混入下の not-separated 寄り。')
with open(path,'w',encoding='utf-8') as f: f.write(data)
print('typo occurrences fixed=', c)
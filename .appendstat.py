#!/usr/bin/env python3
path='.b189_run424_stats.py'
extra='''
    tc = sum(s['cold'] for _, s in out[:3])
    pct = (tc*100) // 60
    print("TOTAL search cold %d/60 (%d%%)" % (tc, pct))
else:
    print("NON-200 present - inspect")
'''
with open(path, 'a', encoding='utf-8') as f:
    f.write(extra)
print('appended')
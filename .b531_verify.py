import unicodedata, sys
data = open('query-cosientist.md', encoding='utf-8').read()
lines = data.split(chr(10))
# find K-Z3 row
kz = -1
for i,L in enumerate(lines):
    if 'K-Z1/K-Z2' in L and len(L) > 100:
        kz = i
        break
cnt = kompile = kz > -1
sub = 'falsify 2026-09-09 (第237回'
print('kz_row', kz+1 if kz >-1 else None, 'has_new_ev', sub in lines[kz] if kz>-1 else False)
# occurrence count of my marker across whole file
whole = sub in data
print('whole_marker_occurrences', whole.Count? if hasattr(whole,'count') else 0)
# iter-log top
for i,L in enumerate(lines[:6]:
    pass
print('top_after_itercheck_skipped')
# combing scan on the two inserted regions
for name,idx0,idx1 in [('kz',kz,kz+1),]:
    seg = lines[kz][-1600:]
    comb = [c for c in seg if unicodedata.combining(c)]
    print(name, 'combining', len(comb))
# iter top lines 411..413
for i in range(410, min(414,len(lines)):
    print('L'+str(i+1), lines[i][:40]
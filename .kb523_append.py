#!/usr/bin/env python3
import io
P='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
TXT=io.open(P,encoding='utf-8').read()
if TXT.startswith('\ufeff'):
    TXT=TXT[1:]
LINES=TXT.split('\n')

def scr(s):
    return s.replace('\u200b','').replace('\u200c','').replace('\u200d','')

ROWIDX=None
for i,l in enumerate(LINES):
    if l.startswith('| K-Z3 '):
        ROWIDX=i
        break
if ROWIDX is None:

    print('KZ3 ROW NOT FOUND')
else:
    ROW=LINES[ROWIDX]
    ev=scr(' 02时台 帯初 run523 (falsify 第233回, host load-1 24-46 混入下: search cold 8/60 ~13.3% (A6+B2+C0/20, 全 200) vs landing control 0/20 完全静穏分離成立。 local 負荷 artifact でないことを control 支持。深夜帯 継続 の cold  ​​再発 継続, rank fold 委ねる (rank 専門)。実行日 02:04 JST。)')
    LINES[ROWIDX]=ROW+ev
    print('EVIDENCE-APPENDED')

HEADIDX=None
for i,l in enumerate(LINES):
    if l.strip().startswith('## Iteration log'):
        HEADIDX=i
        break
if HEADIDX is None:

    print('ITERLOG HEADING NOT FOUND')
else:
    en=scr('- 2026-09-09: falsify 第233回.x 02:04 JST tickしK-Z3 2時台 帯初 run523A-C 測定 (host load-1 24-46 下, search cold 8/60 ~13.3% vs landing control 0/20 完全静穏分離成立、 local 負荷 artifact でない ことを control が支持)。HEAD fa68e24 = falsify 第232回 = remote net-kotobase/main, NEXT 3時台 帯。')
    LINES.insert(HEADIDX+1, en)
    print('ITERLOG-INSERTED')

w=io.open(P,'w',encoding='utf-8')
w.write(('\n'.join(LINES))+'\n')
w.close()

CHK=io.open(P,encoding='utf-8').read()
print('KZ3-COUNT=%d' % CHK.count('| K-Z3 '))
print('EVID-MARK-COUNT=%d' % CHK.count('02时台 帯初 run523'))
print('ITER-ENTRY-COUNT=%d' % CHK.count('falsify 第233回'))
print('ZWSP-COUNT=%d' % (CHK.count('\u200b')+CHK.count('\u200c')+CHK.count('\u200d')))
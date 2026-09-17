import sys

PATH = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
doc = open(PATH, encoding='utf-8').read()
log = []

# --- 1) Relabel my ITER-LOG entry (line starting with '- 2026-09-07: bench 第183回。')
# Search for my iter-log marker and the line it occupies.
m1 = doc.find('- 2026-09-07: bench 第183回。23:04 JST tick。')
if m1 < 0:
    log.append('ERR: bench 第183回 iter-log marker not found')
else:
    nl1 = doc.find('\n', m1)
    line = doc[m1:nl1]
    # safety: only rewrite if this is really my entry (contains 3/60 not 7/60)
    if 'cold(>=0.5s) 3/0/0' not in line:
        log.append('WARN: iter-log line does not read cold 3/0/0; skipping auto-relabel of run id in iter-log')
    else:
        line2 = line.replace('run403', 'run404')
        # adjust header: band-first -> n-add (now 2nd set of 23hr)
        line2 = line2.replace(
            '23時台 (9/7) 帯初計測 run404A–C',
            '23時台 (9/7) n 積み増し run404A–C — run403 は sibling falsify 第176回 (23:04, cold 7/60) が同一窓先行使用のため run404 に読替 (run216/256/263 precedent, 23時台独立計測)')
        line2 = line2.replace('現時刻帯 23時台 (9/7) 帯初計測 run403 を実施',
                              '現時刻帯 23時台 帯初計測 was taken by sibling falsify 第176回 (run403); 本測は次枠 run404 として独立計測')
        # NEXT must advance to run405
        line2 = line2.replace('次 run ID は run404 使用', '次 run ID は run405 使用')
        doc = doc[:m1] + line2 + doc[nl1:]
        log.append('iter-log relabelled to run404')

# --- 2) Relabel my EVIDENCE chunk in K-Z3 row (runs from ' bench 2026-09-07 (第183回,' to end of row)
ev_marker = ' bench 2026-09-07 (第183回, K-Z3 23時台(深夜帯) 帯初計測 run403A–C'
evi = doc.find(ev_marker)
if evi < 0:
    log.append('ERR: evidence chunk marker not found')
else:
    # row end = end of line containing this marker's row (K-Z3 row continues until newline)
    row_end = doc.find('\n', evi)
    chunk = doc[evi:row_end]
    if '3/0/0' not in chunk:
        log.append('WARN: evidence chunk does not contain cold 3/0/0; skipping')
    else:
        chunk2 = chunk.replace('run403', 'run404')
        chunk2 = chunk2.replace(
            '23時台(深夜帯) 帯初計測 run404A–C — rank NEXT 委ねる',
            '23時台(深夜帯) n 積み増し run404A–C — run403 は sibling falsify 第176回 (23:04, 帯初計測 cold 7/60 heavy) が同一時窓で先行録記のため run404 に読替 (run216/256/263 precedent, 23時台の independent 計測として採用可否は rank 判定に委ねる) — rank NEXT 委ねる')
        doc = doc[:evi] + chunk2 + doc[row_end:]
        log.append('evidence chunk relabelled to run404')

open(PATH, 'w', encoding='utf-8').write(doc)
log.append('written OK total_lines=%d' % len(doc.split('\n')))
open('/tmp/bench_relabel.txt', 'w').write('\n'.join(log) + '\n')
print('\n'.join(log))
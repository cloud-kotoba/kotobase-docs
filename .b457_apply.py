# -*- coding: utf-8 -*-
# Append bench record to K-Z3 evidence row (L=279) + insert iter-log entry after '## Iteration log' header.
path = 'query-cosientist.md'
with open(path, encoding='utf-8') as f:
    txt = f.read()

evidence = ' bench 2026-09-08 (\u7b2c203\u56de, K-Z3 11\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run458A-C \u2014 falsify \u7b2c205\u56de run457 (11:02:43\u201311:03:00, 11\u6642\u53f0\u5e2f\u521d 2/60) \u3068\u540c\u6642\u523b\u7a93\u306e\u72ec\u7acb 2 \u8a08\u6e2c\u306e\u305f\u3081 run458 \u306b\u63a1\u756a (run216/256/263 precedent), \u540c\u6e2c\u5b9a\u6cd5 n=20 x 3 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, 11:02\u201311:03 JST, \u5168 80/80 200, host load1 24.55 (11:03 uptime \u5b9f\u6e2c, gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f): cold(>=0.5s) 0/0/0 per 20 = 0/60 \u5b8c\u5168\u9759\u7a4f \u2014 run458A cold 0/20 p50 49.6ms max 155.1ms / run458B cold 0/20 p50 47.9ms max 143.2ms / run458C cold 0/20 p50 44.4ms max 146.9ms, control (kotobase.net/signup) cold 0/20 p50 44.5ms max 126.1ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb (search/control \u3068\u3082 0 cold). run457A \u6563\u767a 2/20 (falsify \u7b2c205\u56de, 10:45) \u306f\u672c\u6e2c\u540c\u6642\u523b\u7a93\u306e 0/60 \u5b8c\u5168\u9759\u7a4f\u3068\u96a3\u63a5\u3057\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u578b\u306e\u5373\u6642\u6e1b\u8870\u3068\u6574\u5408\u300211\u6642\u53f0 (9/8) \u901a\u7b97 = falsify-run457 (2/60) + \u672c\u6e2c run458 (0/60) = 2/120 (~1.7%) \u306e 2 \u30bb\u30c3\u30c8\u4f4e\u301c\u4e2d\u4f4d\u5e2f\u5019\u88dc\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002'

# 1) append to K-Z3 evidence row: the line that starts with '| K-Z3 |'
lines = txt.split('\n')
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'
lines[kz3_idx] = lines[kz3_idx].rstrip() + evidence
print('KZ3_APPAFTER', kz3_idx+1)

# 2) insert iter-log entry right after '## Iteration log' header
hdl = None
for i, ln in enumerate(lines):
    if ln.strip() == '## Iteration log':
        hdl = i
        break
assert hdl is not None, 'iter header not found'
iter_entry = '- 2026-09-08: bench \u7b2c203\u56de\u300211:03 JST tick\u3002K-Z3 11\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run458A\u2013C \u5b9f\u6e2c (falsify \u7b2c205\u56de run457 \u3068\u540c\u6642\u523b\u7a93\u306e\u72ec\u7acb 2 \u8a08\u6e2c\u306e\u305f\u3081 run458 \u306b\u63a1\u756a, run216/256/263 precedent)\u3002live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 24.55 (11:03 uptime \u5b9f\u6e2c, gate 7.5 \u8d85\u904e) \u2014 K-Z3 \u89b3\u6e2c\u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916\u3067\u5b9f\u65bd\u3002cold(>=0.5s) 0/0/0 per 20 = 0/60 \u5b8c\u5168\u9759\u7a4f: run458A/B/C \u3068\u3082 cold 0/20 (p50 49.6/47.9/44.4ms), control (kotobase.net/signup) 0/20 \u5b8c\u5168\u9759\u7a4f (p50 44.5ms max 126.1ms) \u3067 control \u5206\u96e2\u6210\u7acb\u300211\u6642\u53f0 (9/8) \u901a\u7b97 = falsify run457 (2/60) + \u672c tick run458 (0/60) = 2/120 (~1.7%) \u306e 2 \u30bb\u30c3\u30c8\u4f4e\u301c\u4e2d\u4f4d\u5e2f\u5019\u88dc \u2014 \u6563\u767a\u5373\u6d88\u5931\u578b\u7d99\u7d9a (heavy \u306f run331A \u4ee5\u964d\u975e\u518d\u73fe)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u4e0d\u542b\u3002'
lines.insert(hdl+1, iter_entry)
print('ITER_INS_AFTER', hdl+1)

with open(path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print('WROTE_OK')
print('RUN458_COUNT_AFTER', txt.count('run458') if False else open(path,encoding='utf-8').read().count('run458'))
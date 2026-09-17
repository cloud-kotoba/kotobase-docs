import io
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
ev = "falsify 2026-09-17 (\u7b2c162\u56de, K-Z3 11\u6642\u53f0 n\u7a4d\u307f\u5817\u3057 run652A-C, \u540c\u6e2c\u5b9a\u6cd5 n=20 x3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 11:30:08-11:30:23 JST, \u5168 60/60 200 + control 20/20 200, \u6b63 endpoint search.yataverse.com/search?q=test, host load1 9.42 (11:30 \u5b9f\u6e2c, gate 7.5 \u8d85\u900e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b - curl + python3 stats \u306e\u307f): cold(>=0.5s) 3/0/0 per 20 = 3/60 (~5.0%) - run652A cold 3/20 (#3 806.9/#7 690.8/#10 889.4ms \u5206\u6563\u5358\u767a) p50 89.5ms p95 806.9ms max 889.4ms / run652B cold 0/20 p50 56.5ms max 175.0ms / run652C cold 0/20 p50 48.8ms max 143.9ms, landing control (kotoba.cloud/, \u540c\u6642\u523b, n=20, \u5168 200) cold 0/20 p50 89.0ms max 348.7ms \u5b8c\u5168\u9759\u7a4e\u3067 control \u5206\u9694\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002\u305f\u3070\u3093 run652A \u51b7 3/20 \u306f B/C 0/20 \u5373\u6d88\u5931\u3067\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u578b\u7d99\u7d9a\u300211\u6642\u53f0 K-Z4 paired: 9/9 ~1.7% vs 9/10 ~16.7% vs 9/11 ~8.3% vs 9/16 ~14.2% vs 9/17 ~5.0% \u3067\u65e5\u6b21\u5909\u52d5\u5e45\u5927\u3001\u5e2f\u56fa\u6709\u6c34\u6e96\u8aac\u3078\u306e\u53cd\u8a3c\u65b9\u5411\u6750\u6599\u7d99\u7d9a\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9587)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5817\u3057\u7d99\u7d9a, \u6b21 run ID \u306f run653 \u4f7f\u7528)\u3002"
iterline = "- 2026-09-17: falsify \u7b2c162\u56de (11:3x JST tick)\u3002HEAD f84bab1 = fetch \u5f8c net-kotobase/main \u5148\u7aef\u4e00\u81f4 (worktree detached HEAD \u306e\u305f\u3081 fetch net-kotobase + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f, \u4e57\u96e2 0; git pull --ff-only \u306f silent \u5931\u6557\u306e\u305f\u3081\u4e0d\u4f7f\u7528\u624b\u9806)\u3002monitor: host load1 22.06 (11:24 pre-run \u5b9f\u6e2c, gate 7.5 \u8d85\u900e \u2014 production HTTP \u5b9f\u6e2c\u306a\u3089 gate \u5916)\u3002NEXT \u300cK-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5817\u3057\u7d99\u7d9a\u300d\u306f run646/run647 (9/16)\u3067\u6d88\u5316\u6e08\u307f\u306a\u308a stale\u3001\u304b\u3064\u672c tick \u664a\u523b 11\u6642\u53f0\u3067 23\u6642\u53f0\u5f85\u6a5f\u4e0d\u53ef\u80fd\u306a\u305f\u3081\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (production HTTP \u5b9f\u6e2c) \u3067 K-Z3 11\u6642\u53f0 n \u7a4d\u307f\u5817\u3057 run652A-C \u3092\u5b9f\u65bd (\u540c\u6e2c\u5b9a\u6cd5 n=20 x3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 11:30:08-11:30:23 JST, \u5168 80/80 200): cold(>=0.5s) 3/60 (~5.0%) - A 3/20 \u5206\u6563\u5358\u767a (690.8-889.4ms) + B/C 0/20, control (kotoba.cloud/) 0/20 p50 89.0ms max 348.7ms \u5b8c\u5168\u9759\u7a4e\u3067\u5206\u9694\u6210\u7acb\u3002\u672c tick \u524d\u306b run652 \u672a\u4f7f\u7528\u3092 git log \u78ba\u8a8d\u6e08\u307f (grep count 0)\u300211\u6642\u53f0\u65e5\u6b21 paired set \u7d99\u7d9a (9/17 ~5.0%, \u65e5\u6b21\u5909\u52d5\u5e45\u5927 = K-Z4 \u53cd\u8a3c\u65b9\u5411\u6750\u6599)\u3002\u307e\u305f\u3001control \u4fa7 p50 89ms \u306f target warm \u7fa7 (48.8-56.5ms) \u3088\u308a\u9ad8\u4f4d\u3067\u5fdc\u7b54\u5c42\u9055\u3044\u3068\u3082\u306b\u6ce8\u8a18 (cold \u5224\u5b9a\u306f cold>=0.5s \u95a2\u5024\u306e\u307f)\u3002evidence \u306f\u672c\u30d5\u30a1\u30a4\u30eb\u672b\u5c3e\u306b\u8ffd\u8a18\u6e08\u307f\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9587)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5817\u3057\u7d99\u7d9a, \u6b21 run ID \u306f run653 \u4f7f\u7528)\u3002secret \u4e0d\u542b (curl + python3 stats \u306e\u307f)\u3002"
with io.open(p, encoding='utf-8') as f:
    lines = f.readlines()
# sanity: no duplicate run652
assert sum(1 for l in lines if 'run652' in l) == 0, 'dupe run652'
# insert iter line right after '## Iteration log'
idx = None
for i, l in enumerate(lines):
    if l.startswith('## Iteration log'):
        idx = i
        break
assert idx is not None, 'no iteration log header'
lines.insert(idx+1, iterline + '\n')
# append evidence at file end
if lines[-1].strip():
    lines.append('\n')
lines.append(ev + '\n')
with io.open(p, 'w', encoding='utf-8') as f:
    f.writelines(lines)
# verify
with io.open(p, encoding='utf-8') as f:
    txt = f.read()
print('run652 occurrences:', txt.count('run652'))

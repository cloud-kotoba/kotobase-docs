import re, sys
p = 'query-cosientist.md'
text = open(p).read()

ev = "  falsify run649 9/17 03:24 JST K-Z3 3\u6642\u53f0 n\u7a4d\u307f\u5897\u3057 (n=20\u00d73 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, search.yataverse.com/search?q=test, \u5168 60/60 200 + control 20/20 200): cold(\u22650.5s) 8/60 (~13.3%) - A 7/20 \u5c3e\u90e8\u96c6\u4e2d (idx14-20 \u9023\u7d9a cold 693-1039ms, \u7a81\u767a\u30d1\u30bf\u30fc\u30f3\u5178\u578b) + B 0/20 + C 1/20 \u672b\u5c3e\u5358\u767a 1118ms, control (kotoba.cloud/) 0/20 p50 191ms max 309ms \u5b8c\u5168\u5206\u96e2\u6210\u7acb. \u63a2\u982d probe: search.kotobase.net \u306f non-200 \u306e\u305f\u3081\u4e0d\u63a1\u7528. 3\u6642\u53f0\u521d\u6e2c\u5b9a\u306e\u305f\u3081\u540c\u5e2f\u65e5\u5dee\u5bfe\u7167\u306f\u672a\u5b58 (K-Z4 paired \u5f85\u6a5f\u7d99\u7d9a). status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b."

if text.rstrip().endswith(ev[:40]):
    sys.exit('dup')
new = text.rstrip('\n') + '\n\n' + ev + '\n'
open(p, 'w').write(new)

# iter log: insert right after '## Iteration log' heading line
lines = new.split('\n')
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        entry = ("- 2026-09-17: falsify \u7b2c161\u56de (03:2x JST tick)\u3002HEAD a9a93c0 = fetch \u5f8c net-kotobase/main \u5148\u7aef\u4e00\u81f4 (worktree detached HEAD \u306e\u305f\u3081 fetch net-kotobase + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f, \u4e56\u96e2 0)\u3002monitor: host load1 15.84 (03:23 pre-run \u5b9f\u6e2c, gate 7.5 \u8d85\u904e \u2014 production HTTP \u5b9f\u6e2c\u306a\u3089 gate \u5916), live smoke 301/301\u3002NEXT \u59d4\u306d\u308b\u306b\u3064\u304d\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (production HTTP \u5b9f\u6e2c) \u3067 K-Z3 3\u6642\u53f0 run649A-C \u5b9f\u65bd (\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 03:24:06-03:24:31 JST, \u5168 60/60 200 + control 20/20 200): cold(\u22650.5s) 8/60 (~13.3%) - A 7/20 \u5c3e\u90e8\u96c6\u4e2d (idx14-20 \u9023\u7d9a cold 693-1039ms) + B 0/20 + C 1/20, control 0/20 \u5b8c\u5168\u5206\u96e2\u3002evidence \u306f\u672c\u30d5\u30a1\u30a4\u30eb\u672b\u5c3e\u306b\u8ffd\u8a18\u6e08\u307f\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e26 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a, \u6b21 run ID \u306f run650 \u4f7f\u7528)\u3002secret \u4e0d\u542b (curl + python3 stats \u306e\u307f)\u3002")
        lines.insert(i + 1, entry)
        open(p, 'w').write('\n'.join(lines))
        break
else:
    sys.exit('no heading')

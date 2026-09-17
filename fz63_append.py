import io, re

path = 'query-cosientist.md'
lines = open(path, encoding='utf-8').readlines()

ev = (" falsify 2026-09-05 (\u7b2c63\u56de, K-Z3 20\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c run167A\u2013C, \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, "
      "\u5225\u63a5\u7d9a curl TTFB+http_code, Tokyo, 20:18:10\u201320:18:33 JST, \u5168 80/80 200, host load1 43.56 \u306f production HTTP "
      "\u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): run167A cold(>=0.5s) 0/20 p50 0.149s (max 0.301s) / run167B cold 0/20 p50 0.074s / "
      "run167C cold 0/20 p50 0.082s (max 0.477s) \u2014 landing control \u3082 cold 0/20 p50 0.119s (max 0.238s) \u3067 cold \u5b9a\u7fa9\u3067\u306f "
      "\u5168 80 \u8a66\u884c\u5b8c\u5168\u9759\u7a33\u3060\u304c search/control \u4e21\u7fa4\u304c\u540c\u6642\u306b 70\u2013150ms \u5e2f\u306b\u4e0a\u632f\u308c\u3057 run158 \u578b\u90e8\u5206\u5168\u4f53\u9045\u5ef6\u7a93\u306e"
      "\u53ef\u80fd\u6027 (partially not-separated \u2014 run158 \u524d\u4f8b\u306b\u5f93\u3044\u5e2f\u767a\u73fe\u7387\u3078\u306e warm \u5074\u63a1\u7528\u53ef\u5426\u306f rank \u5224\u65ad)\u3002"
      "20\u6642\u53f0\u306f\u5e2f\u521d\u8a08\u6e2c\u3067 0/60 \u4f4e\u4f4d\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")

idx = 205
row = lines[idx]
assert row.startswith('| K-Z3 | worker |'), f'line 206 is not K-Z3: {row[:60]}'
if row.rstrip().endswith('|'):
    lines[idx] = row.rstrip()[:-1].rstrip() + ev + ' |\n'
else:
    lines[idx] = row.rstrip('\n') + ev + '\n'

src = ''.join(lines)
m = re.search(r'^#+ *Iteration log.*$', src, re.M)
assert m, 'iteration log heading not found'
insert_at = src.find('\n', m.end()) + 1
entry = ("- 2026-09-05: falsify \u7b2c63\u56de\u3002rank NEXT\u300c\u59d4\u306d\u308b\u300d\u306e\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (K-Z3 \u73b0\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057) \u3092\u53d7\u3051\u3001"
         "K-Z3 20\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c run167A\u2013C \u3092\u540c\u6e2c\u5b9a\u6cd5\u3067\u5b9f\u65bd (20:18 JST, production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
         "secret \u4e0d\u542b): search cold(>=0.5s) 0/60 \u5b8c\u5168\u9759\u7a33\u3060\u304c p50 74\u2013149ms \u3068 landing control (p50 119ms, cold 0/20) \u3068\u540c\u6642\u4e0a\u632f\u308c\u306e "
         "run158 \u578b\u90e8\u5206\u5168\u4f53\u9045\u5ef6\u7a93\u306e\u53ef\u80fd\u6027 (partially not-separated) \u2014 20\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c\u3002status \u9077\u79fb\u306a\u3057 (rank \u5c02\u9580)\u3002"
         "NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73b0\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d99\u7d9c)\u3002\n")
src = src[:insert_at] + entry + src[insert_at:]

open(path, 'w', encoding='utf-8').write(src)
print('OK kz3 row has ev:', 'falsify 2026-09-05 (\u7b2c63\u56de' in src)
print('OK log entry present:', 'falsify \u7b2c63\u56de' in src)

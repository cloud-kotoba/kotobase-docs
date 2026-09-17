import io

path = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with io.open(path, 'r', encoding='utf-8') as f:
    text = f.read()

anchor = '| open | falsify 2026-09-05 (K-Z3 18\u6642\u53f0 control \u4ed8\u304d\u518d\u8a08\u6e2c run159A\u2013C'
assert text.count(anchor) == 1, f"anchor count = {text.count(anchor)}"

evidence = ('falsify 2026-09-05 (K-Z3 18\u6642\u53f0 control \u4ed8\u304d\u8ffd\u52a0 n run161A\u2013C, run159 \u76f4\u5f8c\u306e\u8ffd\u52a0 n, '
            '\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 18:48:04\u201318:48:13 JST, \u5168 80/80 200, '
            'host load1 47.09 \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): run161A cold(>=0.5s) 0/20 p50 0.045s (max 0.292s) / '
            'run161B cold 0/20 p50 0.039s / run161C cold 0/20 p50 0.043s (max 0.324s) \u2014 '
            'landing control (kotobase.net/, \u540c\u6642\u523b, n=20, \u5168 200) \u306f cold 0/20 p50 0.055s (max 0.105s) \u3068\u9759\u7a33\u3067 '
            'control \u5206\u96e2\u6210\u7acb\u3002\u5168 3 run \u5b8c\u5168\u9759\u7a33 (run157 \u306b\u7d9a\u304f 18\u6642\u53f0 2 \u30bb\u30c3\u30c8\u76ee\u306e 0/60)\u3002'
            '18\u6642\u53f0\u901a\u7b97\u306f run159A\u2013C (1/60) + \u672c tick (0/60) \u3067 120 \u8a66\u884c\u4e2d 1 \u8a66\u884c (~0.8%) \u306e\u4f4e\u4f4d\u5e2f \u2014 '
            'run158 \u306e not-separated \u5206\u306f\u63a1\u7528\u4e0d\u53ef\u3068\u3059\u308c\u3070\u3001run158 \u578b\u5168\u4f53\u9045\u5ef6\u7a93\u306f 15\u201330 \u5206\u9593\u9694\u3067\u5373\u6642\u975e\u518d\u73fe\u306e\u5c40\u6240\u7684\u77ed\u6642\u9593\u7a93\u3068\u3057\u3066 '
            '\u5e2f\u767a\u73fe\u7387\u306b\u306f\u53cd\u6620\u3055\u308c\u306a\u3044\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002 ')

text = text.replace(anchor, '| open | ' + evidence + 'falsify 2026-09-05 (K-Z3 18\u6642\u53f0 control \u4ed8\u304d\u518d\u8a08\u6e2c run159A\u2013C', 1)

with io.open(path, 'w', encoding='utf-8') as f:
    f.write(text)
print('appended OK')

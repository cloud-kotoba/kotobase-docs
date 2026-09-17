src = open('query-cosientist.md', encoding='utf-8').read()
# sanity: ensure our K-Z3 evidence & iteration entry are intact and file ends with newline
print('has ev:', 'falsify 2026-09-05 (\u7b2c63\u56de, K-Z3 20\u6642\u53f0\u5e2f\u521d\u8a08\u6e2c run167A' in src)
print('has log:', '- 2026-09-05: falsify \u7b2c63\u56de' in src)
print('ends with newline:', src.endswith('\n'))
# check only our rows were touched: count simplified chars remaining anywhere near our insert
import re
moji = re.findall('[\u7a33\u5e26\u73b0\u7d9c]', src)
print('simplified chars anywhere:', len(moji))
for m in re.finditer('[\u7a33\u5e26\u73b0\u7d9c]', src):
    print(src[max(0,m.start()-30):m.start()+30].replace('\n',' '))

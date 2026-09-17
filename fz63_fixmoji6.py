src = open('query-cosientist.md', encoding='utf-8').read()
i = src.find('falsify 2026-09-05 (\u7b2c63\u56de')
seg_end = src.find('rank \u5c02\u9580)\u3002', i) + len('rank \u5c02\u9580)\u3002')
seg = src[i:seg_end]
before = seg
seg = seg.replace('\u7a33', '\u7a4f')  # simplified 稳 -> 穏
seg = seg.replace('\u5e26', '\u5e2f')
seg = seg.replace('\u73b0', '\u73fe')
src = src[:i] + seg + src[seg_end:]
open('query-cosientist.md', 'w', encoding='utf-8').write(src)
src2 = open('query-cosientist.md', encoding='utf-8').read()
print('changed:', before != seg)
# global check within our inserted fragments
print('simplified remaining in ev seg:', any(c in seg for c in '\u7a33\u5e26\u73b0'))

src = open('query-cosientist.md', encoding='utf-8').read()
j = src.find('- 2026-09-05: falsify \u7b2c63\u56de')
assert j != -1
k = src.find('\n', j)
entry = src[j:k]
# inspect code points of suspicious chars
sus = []
for ch in entry:
    if ch in ('\u73b0', '\u9759\u7a33'[:1], '\u7a33', '\u7d9c', '\u7efc'):
        pass
    cp = ord(ch)
    if ch in '\u73b0\u7a33\u7d9c\u7efc\u5e26':
        sus.append((ch, hex(cp)))
print('suspicious:', sus)
# fix: 现在時刻帯 uses U+73B0 (simplified 现) — replace with 現 U+73FE
entry2 = entry.replace('\u73b0', '\u73fe')
# 静稳 uses 稳 U+7A33 (simplified) — replace with 穏 U+7A4F
entry2 = entry2.replace('\u7a33', '\u7a4f')
# 継綜 uses 綜 U+7D9C — should be 継続 (続 U+7D9A)
entry2 = entry2.replace('\u7d9c', '\u7d9a')
# 帯 U+5E26? simplified 带 is U+5E26; correct 带 Japanese is U+5E2F
entry2 = entry2.replace('\u5e26', '\u5e2f')
src = src[:j] + entry2 + src[k:]
open('query-cosientist.md', 'w', encoding='utf-8').write(src)
print(repr(src[j:j+400]))

text = open('query-cosientist.md', encoding='utf-8').read()
zw = sum(1 for ch in text if '\u200b' <= ch <= '\u200f')
lines = text.split('\n')
kz=lines[278]
print('zerowidth', zw)
print('kz3_end', repr(kz[-320:]))
print('ilog_top', repr(lines[400:403]))
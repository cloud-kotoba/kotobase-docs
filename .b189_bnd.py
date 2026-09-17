import io
s = io.open('query-coscientist.md', encoding='utf-8').read()
i = s.find('NEXT: 委ねる (rank 指定優先')
print(repr(s[i:i+90]))))
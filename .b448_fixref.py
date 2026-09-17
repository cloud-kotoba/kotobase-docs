#!/usr/bin/env python3
md = open('query-cosientist.md', encoding='utf-8').read()
old = "HEAD 9797280 = falsify 第198回 (09:50, K-Z3 9時台 n-add run447 cold 2/60, 9時台 3 セット目)"
new = "HEAD c860379 = rank 第198回 (09:51, fold run446+run447 -> 9時台 9/180 ~5.0%; HEAD 9797280 = falsify 第198回 run447 済)"
assert md.count(old) == 1, md.count(old)
md = md.replace(old, new)
open('query-cosientist.md', 'w', encoding='utf-8').write(md)
print('fixed HEAD ref -> c860379')
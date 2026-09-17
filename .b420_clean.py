def clean(t):
    r=[]
    for c in t:
        o=ord(c)
        if 0x200b<=o<=0x200d:
            r.append('')
            continue
        if 0x0300<=o<=0x036F or o==0xFEFF:
            continue
        r.append(c)
    return ''.join(r)
for f in ['/tmp/fal_ev420.txt','/tmp/fal_iter420.txt']:
    t=open(f,encoding='utf8'(.read())
    open(f,'w',encoding='utf8'(.write(clean(t))
print('done')
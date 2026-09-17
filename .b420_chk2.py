s=open('.b420_runner.sh','rb').read()
bad=[]
for i in range(len(s)):
    o=s[i]
    if o>=0x80:
        bad.append((i,hex(o))))
print('nonascii_count',len(bad))
print(bad[:10])
# check tilde-like around max-time
idx=s.find(b'max-time')
print('max-time bytes:',s[idx:idx+14])
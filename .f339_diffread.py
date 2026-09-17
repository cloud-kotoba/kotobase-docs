d=open('/tmp/fal_full.txt').read()
adds=[l[1:] for l in d.splitlines() if l.startswith('+') and not l.startswith('+++')]
dels=[l[1:] for l in d.splitlines() if l.startswith('-') and not l.startswith('---')]
print('ADD',len(adds),'DEL',len(dels))
for a in adds: print('  +',a[:70].replace(chr(10),' '))
for a in dels: print('  -',a[:70].replace(chr(10),' '))
# trailing newline check
print('ends with newline:', open('query-cosientist.md').read().endswith('\n'))
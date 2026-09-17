import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
# compare pushed HEAD file vs origin/main previous (07e493e)
def line_at(rev):
    txt = subprocess.run(['git','show',f'{rev}:query-cosientist.md'],cwd=d,capture_output=True,text=True).stdout.splitlines()
    kz3 = [l for l in txt if l.startswith('| K-Z3')]
    it = [l for l in txt if l.startswith('- 2026-09-05: bench') or l.startswith('- 2026-09-05: rank') or l.startswith('- 2026-09-05: falsify')]
    return kz3, [x[:80] for x in it]
for rev in ['07e493e','HEAD']:
    kz3, it = line_at(rev)
    print('REV', rev)
    print('  K-Z3 evidence ends with:', kz3[0][-260:] if kz3 else 'NONE')
    print('  iteration log lines:', len(it), it[:3])

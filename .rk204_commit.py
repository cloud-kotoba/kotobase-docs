import io, subprocess
p = 'query-cosientist.md'
out = io.open('/tmp/commit.txt', 'w', encoding='utf-8')

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return (r.returncode, r.stdout, r.stderr)

rc, so, se = run(['git','add','--','query-cosientist.md'])
out.write('add rc=%d %s %s\n' % (rc, so, se))
rc, so, se = run(['git','commit','-m','rank 第204回: K-Z3 11時台 fold run460(4/60)+run461(2/60) -> 13/300 ~4.3% 5セット; status/rank/evolve unchanged; NEXT K-Z3 11時台 n-add run462'])
out.write('commit rc=%d %s %s\n' % (rc, so[:200], se[:200]))
rc, so, se = run(['git','rev-parse','HEAD'])
out.write('after commit HEAD: %s\n' % so.strip())
out.close()
print('done')
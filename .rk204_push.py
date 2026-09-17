import io, subprocess
out = io.open('/tmp/push.txt', 'w', encoding='utf-8')

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return (r.returncode, r.stdout, r.stderr)

rc, so, se = run(['git','rev-parse','HEAD'])
out.write('local HEAD: %s\n' % so.strip())
# stable ref push of HEAD to remote main
rc, so, se = run(['git','push','bench_fetch','HEAD:main'])
out.write('push rc=%d\nstdout: %s\nstderr: %s\n' % (rc, so, se))
out.close()
print('done')
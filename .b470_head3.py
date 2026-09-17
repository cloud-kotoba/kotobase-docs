import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = []
def run(args, timeout=15):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return 'exit=%d %s %s' % (r.returncode, r.stdout.strip()[:3000], r.stderr.strip()[:1000])
    except subprocess.TimeoutExpired:
        return 'TIMEOUT'
    except Exception as e:
        return 'ERR %s' % e
# is HEAD (=rank 211) pushed remote?
out.append('REMOTE_HEAD:' + run(['git','rev-parse','net-kotobase/main']))
out.append('HEAD:' + run(['git','rev-parse','HEAD']))
out.append('LOG3:' + run(['git','log','--oneline','-3']).replace('\n',' | '))
# verify my content in HEAD version of file
out.append('HEAD_has_falsify212_iter:' + run(['git','show','HEAD:query-cosientist.md'], ) + '')
out.append('DIFFSTAT:' + run(['git','diff','HEAD','--stat']))
with open('/tmp/f_head3.log','w') as f:
    f.write('\n'.join(out))
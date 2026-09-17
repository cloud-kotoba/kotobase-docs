import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = []
def run(args, timeout=15):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return (r.returncode, r.stdout.strip(), r.stderr.strip())
    except subprocess.TimeoutExpired:
        return ('TIMEOUT','','')
    except Exception as e:
        return ('ERR','%s'%e,'')
rc, so, se = run(['git','rev-parse','net-kotobase/main'])
out.append('REMOTE_MAIN=%s [%s]' % (so, rc))
rc, so, se = run(['git','rev-parse','HEAD'])
out.append('HEAD=%s [%s]' % (so, rc))
rc, so, se = run(['git','diff','HEAD','--stat'])
out.append('DIFFSTAT=[%s]%s' % (rc, so))
rc, so, se = run(['git','log','--oneline','-2'])
out.append('LOG2=%s' % so.replace('\n',' | '))
with open('/tmp/f_head_remote.log','w') as f:
    f.write('\n'.join(out))
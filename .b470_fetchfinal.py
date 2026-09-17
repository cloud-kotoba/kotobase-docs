import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = []
def run(args, timeout=40):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return (r.returncode, r.stdout.strip(), r.stderr.strip())
    except subprocess.TimeoutExpired:
        return ('TIMEOUT','','')
    except Exception as e:
        return ('ERR','','%s'%e)
rc, so, se = run(['git','fetch','net-kotobase','main'])
out.append('FETCH [%s] %s %s' % (rc, so.replace('\n',' | '), se.replace('\n',' | ')[:300]))
rc, so, se = run(['git','rev-parse','net-kotobase/main'])
out.append('REMOTE_NOW=%s [%s]' % (so, rc))
rc, so, se = run(['git','rev-parse','HEAD'])
out.append('HEAD=%s [%s]' % (so, rc))
with open('/tmp/f_fetch_final.log','w') as f:
    f.write('\n'.join(out))
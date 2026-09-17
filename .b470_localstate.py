import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = []
def run(args, timeout=10):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return 'exit=%d %s %s' % (r.returncode, r.stdout.strip(), r.stderr.strip())
    except Exception as e:
        return 'ERR %s' % e
out.append('HEAD=' + run(['git','rev-parse','HEAD']))
out.append('FETCH_HEAD=' + run(['git','rev-parse','FETCH_HEAD']))
out.append('LOG:' + run(['git','log','--oneline','-3']).replace('\n',' | '))
out.append('DIFF:' + run(['git','diff','HEAD','--stat']))
out.append('DIFFCACHED:' + run(['git','diff','--cached','--stat']))
out.append('STATUS:' + run(['git','status','--short']))
with open('/tmp/f_state.log','w') as f:
    f.write('\n'.join(out))
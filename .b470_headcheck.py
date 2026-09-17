import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out = []
def run(args, timeout=15):
    try:
        r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
        return 'exit=%d %s %s' % (r.returncode, r.stdout.strip()[:2000], r.stderr.strip()[:2000])
    except subprocess.TimeoutExpired:
        return 'TIMEOUT'
    except Exception as e:
        return 'ERR %s' % e
out.append('SHOW_HEAD:' + run(['git','show','--stat','--oneline','HEAD']))
out.append('HEAD_TRACK:' + run(['git','log','--oneline','-4']))
out.append('DIFFHEAD:' + run(['git','diff','HEAD','--stat']))
with open('/tmp/f_head2.log','w') as f:
    f.write('\n'.join(out))
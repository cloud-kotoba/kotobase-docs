import subprocess
r = subprocess.run(['git', 'fetch', 'net-kotobase', 'main'], capture_output=True, text=True, cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
with open('/tmp/f_fetch5.log', 'w') as f:
    f.write('fetch_exit=%d\n' % r.returncode)
    f.write(r.stdout)
    f.write(r.stderr)
    f.write('REMOTE=%s\n' % subprocess.run(['git','rev-parse','net-kotobase/main'],capture_output=True,text=True,cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs').stdout.strip())
    f.write('HEAD=%s\n' % subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True,cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs').stdout.strip())
    st = subprocess.run(['git','status','--short'],capture_output=True,text=True,cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
    f.write('STATUS:\n' + st.stdout + st.stderr)
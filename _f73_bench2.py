import subprocess
cwd = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
out = subprocess.run(['git', 'show', 'def7b19', '--', 'query-cosientist.md'],
                     capture_output=True, text=True, cwd=cwd)
adds = [l for l in out.stdout.split('\n') if l.startswith('+') and 'bench 第73回' in l]
full = adds[0][1:] if adds else 'NOT FOUND'
with open('_f73_bench2.txt', 'w') as f:
    f.write(full)
print(len(full))

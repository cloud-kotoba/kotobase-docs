import subprocess

repo = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
r = subprocess.run(['git', 'push', 'net-kotobase', 'HEAD'], cwd=repo, capture_output=True, text=True)
print('rc', r.returncode)
print(r.stdout[-600:])
print(r.stderr[-600:])

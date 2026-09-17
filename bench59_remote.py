import subprocess

repo = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
r = subprocess.run(['git', 'remote', '-v'], cwd=repo, capture_output=True, text=True)
print(r.stdout, r.stderr)

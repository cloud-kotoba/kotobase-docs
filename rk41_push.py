import subprocess
r = subprocess.run(['git', 'push', 'net-kotobase', 'HEAD:main'], capture_output=True, text=True)
print('PUSH_RC', r.returncode)
print(r.stdout)
print(r.stderr)

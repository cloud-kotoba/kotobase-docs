import subprocess
r = subprocess.run(['git', 'fetch', 'net-kotobase'], capture_output=True, text=True)
r2 = subprocess.run(['git', 'ls-remote', 'net-kotobase', 'main'], capture_output=True, text=True)
r3 = subprocess.run(['git', 'log', '--oneline', '-3', 'net-kotobase/main'], capture_output=True, text=True)
open('fz63_verify_out.txt', 'w').write(f"ls-remote:\n{r2.stdout}{r2.stderr}\nlog:\n{r3.stdout}{r3.stderr}\n")
print('ok')

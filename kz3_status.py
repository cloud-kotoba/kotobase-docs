import subprocess, sys
r = subprocess.run('date; uptime; wc -l kz3_run97_out.txt', shell=True, capture_output=True, text=True)
sys.stdout.write(r.stdout + r.stderr)

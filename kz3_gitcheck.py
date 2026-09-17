import subprocess, sys
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    sys.stdout.write(r.stdout + r.stderr)
run('git log --oneline -3')
run('git status --short')
run('grep -c run96A query-cosientist.md')

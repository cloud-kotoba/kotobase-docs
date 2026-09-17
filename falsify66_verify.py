import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
r = subprocess.run(['git', 'show', '--stat', 'HEAD'], cwd=d, capture_output=True, text=True)
r2 = subprocess.run(['git', 'show', 'HEAD', '--', 'query-cosientist.md'], cwd=d, capture_output=True, text=True)
diff = r2.stdout
# show only the changed lines (skip huge context)
changed = [l for l in diff.splitlines() if l.startswith('+') or l.startswith('-')]
open(d + '/falsify66_verify.txt', 'w').write(r.stdout + '\n--- changed lines (first 40) ---\n' + '\n'.join(changed[:40]) + '\n\n--- full diff head ---\n' + diff[:3000])

#!/usr/bin/env python3
import subprocess
out = subprocess.run(['git', 'diff', '--unified=0', 'query-cosientist.md'],
                     capture_output=True, text=True)
open('/tmp/b448_diff2.txt', 'w').write(out.stdout)
# summarize added/removed line markers
added = [l for l in out.stdout.split('\n') if l.startswith('+') and not l.startswith('+++')]
removed = [l for l in out.stdout.split('\n') if l.startswith('-') and not l.startswith('---')]
print('added_lines:', len(added))
print('removed_lines:', len(removed))
for l in removed:
    print('REM:', l[:80])
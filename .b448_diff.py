#!/usr/bin/env python3
import subprocess
out = subprocess.run(['git', 'diff', '--unified=1', 'query-cosientist.md'],
                     capture_output=True, text=True)
open('/tmp/b448_diff.txt', 'w').write(out.stdout)
print('rc', out.returncode, 'len', len(out.stdout))
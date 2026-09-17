# -*- coding: utf-8 -*-
import subprocess
out = subprocess.run(['git', 'diff', '--unified=0', '--', 'query-cosientist.md'],
                     capture_output=True, text=True)
with open('.b499_showdiff.txt', 'w', encoding='utf-8') as f:
    f.write(out.stdout)
    f.write('\n===STDERR===\n')
    f.write(out.stderr)
print('wrote', len(out.stdout))
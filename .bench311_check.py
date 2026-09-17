#!/usr/bin/env python3
import subprocess
# verify run311 not already measured
data = open('query-cosientist.md', encoding='utf-8').read()
for tok in ['run311A-C','run311A','run311']:
    print(tok, 'count', data.count(tok))
print('HEAD', subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True).stdout.strip())
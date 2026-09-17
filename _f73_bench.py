import subprocess
out = subprocess.run(['git', 'show', 'def7b19', '--', 'query-cosientist.md'],
                     capture_output=True, text=True,
                     cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
text = out.stdout
# extract just the added line
adds = [l[1:600] for l in text.split('\n') if l.startswith('+') and not l.startswith('+++')]
with open('_f73_bench.txt', 'w') as f:
    f.write('\n----\n'.join(adds))
print('adds:', len(adds))

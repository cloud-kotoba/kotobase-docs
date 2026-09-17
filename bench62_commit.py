import subprocess
def run(*cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    print(' '.join(cmd), '=> rc', r.returncode)
    print((r.stdout or '')[-1200:])
    if r.stderr: print('ERR', r.stderr[-600:])
run('git','add','query-cosientist.md','bench62_kq1_n30.mjs','bench62_kq1_n30_out.json','bench62_kq1_reprobe_out.json','bench62_append.py','bench62_append_out.txt','bench62_find.py','bench62_find_out.txt','bench62_ls.py','bench62_ls_out.txt')
run('git','commit','-m','bench iteration 62: K-Q1 x-kotobase-kv-stats header arrival confirmed 30/30 (bench49 method, authenticated query)')
run('git','push','origin','HEAD:net-kotobase')
r = subprocess.run(['git','log','--oneline','-2'],capture_output=True,text=True)
print(r.stdout)

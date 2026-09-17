import io, subprocess
FN = 'query-cosientist.md'
# worktree line 279 (index 278)
wt = io.open(FN, 'r', encoding='utf-8', newline='').read().split('\n')[278]
# HEAD version via git show
p = subprocess.run(['git', 'show', 'HEAD:' + FN], capture_output=True, text=True)
hd = p.stdout.split('\n')[278]
o = io.open('.c151_cmp.txt', 'w', encoding='utf-8')
o.write("HEAD line279 len: %d\n" % len(hd))
o.write("HEAD line279 last 80:\n%s\n" % hd[-80:])
o.write("HEAD line279 last 5 repr: %r\n" % hd[-5:])
o.write("---\n")
o.write("WORKTREE line279 len: %d\n" % len(wt))
o.write("WORKTREE line279 last 5 repr: %r\n" % wt[-5:])
# confirm wt == hd with EVID inserted once
o.write("wt startswith hd[:100]: %s\n" % (wt[:100] == hd[:100]))
o.write("hd ends in wt's region: %s\n" % (hd in wt or hd[-30:] in wt))
o.close()
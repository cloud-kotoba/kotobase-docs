import subprocess, difflib

# get current worktree line and HEAD line for the K-Z3 open hypothesis row (line ~276)
head_blob = subprocess.run(['git','show','HEAD:query-cosientist.md'],capture_output=True,text=True).stdout
wt = open('query-cosientist.md',encoding='utf8').read()

def extract_kz3(text):
    # find the K-Z3 open hypothesis row start
    for line in text.split('\n'):
        if line.startswith('| K-Z3 |'):
            return line
    return None

h = extract_kz3(head_blob)
w = extract_kz3(wt)
print("=== HEAD K-Z3 row present:", h is not None)
print("=== WORKTREE K-Z3 row present:", w is not None)
if h and w:
    print("=== equal:", h==w)
    if h!=w:
        sm = difflib.SequenceMatcher(None, h, w)
        for tag,i1,i2,j1,j2 in sm.get_opcodes():
            if tag!='equal':
                print(f"--- {tag} HEAD[{i1}:{i2}] vs WT[{j1}:{j2}]")
                print("HEAD:", repr(h[i1:i2]))
                print("WT  :", repr(w[j1:j2]))

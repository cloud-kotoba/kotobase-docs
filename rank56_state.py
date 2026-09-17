import subprocess
def run(*args):
    r = subprocess.run(args, capture_output=True, text=True)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
out = []
for c in [["git","status","-sb"],["git","branch","--show-current"],
          ["git","log","--oneline","-2"],["git","rev-parse","HEAD"],
          ["git","rev-parse","net-kotobase/main"]]:
    rc,o,e = run(*c); out.append(f"$ {' '.join(c)}\nRC={rc}\n{o}\n{e}\n---")
open("/tmp/rank56_state.txt","w").write("\n".join(out))

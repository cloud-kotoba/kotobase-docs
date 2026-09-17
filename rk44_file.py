import subprocess, os
out = []
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out.append("exists: %s" % os.path.exists(p))
if os.path.exists(p):
    out.append("size: %d" % os.path.getsize(p))
    txt = open(p, encoding="utf-8", errors="replace").read()
    out.append("chars: %d, lines: %d" % (len(txt), txt.count("\n")+1))
    out.append("=== head 40 lines ===")
    out.extend(txt.splitlines()[:40])
    out.append("=== tail 30 lines ===")
    out.extend(txt.splitlines()[-30:])
r = subprocess.run(["git","status","--porcelain","--","query-cosientist.md"], capture_output=True, text=True, cwd=os.path.dirname(p))
out.append("git status of file: %r" % r.stdout)
r2 = subprocess.run(["git","diff","--stat","HEAD","--","query-cosientist.md"], capture_output=True, text=True, cwd=os.path.dirname(p))
out.append("diff stat vs HEAD: %r %r" % (r2.stdout, r2.stderr))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_file_out.txt","w").write("\n".join(str(x) for x in out))

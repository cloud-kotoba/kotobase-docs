import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
out=[]
out.append("HEAD: "+subprocess.run(['git','rev-parse','HEAD'],capture_output=True,text=True).stdout.strip())
out.append("REMOTE: "+subprocess.run(['git','rev-parse','bench_fetch/main'],capture_output=True,text=True).stdout.strip())
out.append("MDSTATUS: "+subprocess.run(['git','status','--porcelain','query-cosientist.md'],capture_output=True,text=True).stdout.strip())
with open('query-cosientist.md') as f:
    lines=f.readlines()
# find '## Iteration log' header line index
hdr=None
for i,l in enumerate(lines):
    if l.startswith('## Iteration log'):
        hdr=i; break
out.append("HDR_LINE:"+str(hdr+1))
# print next 2 non-blank lines after header
cnt=0
for i in range(hdr+1, len(lines)):
    s=lines[i].strip()
    if s.startswith('- '):
        out.append(f"ENT{i+1}: {s[0:70]}")
        cnt+=1
        if cnt>=3: break
with open('/tmp/r156_restate.txt','w') as f:
    f.write("\n".join(out)+"\n")
print("ok")
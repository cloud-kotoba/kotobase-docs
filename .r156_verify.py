# -*- coding: utf-8 -*-
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
def run(args):
    r=subprocess.run(args,capture_output=True,text=True)
    return r.returncode, r.stdout.strip(), r.stderr.strip()
rc,head,_=run(['git','rev-parse','HEAD'])
rc,remote,_=run(['git','fetch','bench_fetch'])
# re-read
rc,remmain,_=run(['git','rev-parse','bench_fetch/main'])
rc2,newon,_=run(['git','log','--oneline','HEAD..bench_fetch/main'])
rc3,mdstat,_=run(['git','status','--porcelain','query-cosientist.md'])
# check entry in working tree and in remote commit's file
with open('query-cosientist.md') as f:
    txt=f.read()
in_work = ('rank 第156回' in txt)
rc4,remtxt,_=run(['git','show','bench_fetch/main:query-cosientist.md'])
in_remote = ('rank 第156回' in remtxt)
out=[]
out.append("LOCAL HEAD: "+head)
out.append("REMOTE main: "+remmain)
out.append("NEW ON REMOTE (HEAD..main): "+str(newon))
out.append("MD working status: "+repr(mdstat))
out.append("entry in working tree: %s"%in_work)
out.append("entry in remote-main md: %s"%in_remote)
# show top log
rc5,log,_=run(['git','log','--oneline','-4'])
out.append("LOG:\n"+log)
with open('/tmp/r156_verify.txt','w') as f:
    f.write("\n".join(out)+"\n")
print("verify done")
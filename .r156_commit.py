# -*- coding: utf-8 -*-
import subprocess, os, sys
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
LOG=[]
def run(args, check=True):
    r=subprocess.run(args,capture_output=True,text=True)
    LOG.append("CMD: "+" ".join(args)+"\nRC:"+str(r.returncode)+"\n"+r.stdout.strip()+"\n"+r.stderr.strip())
    if check and r.returncode!=0:
        raise SystemExit(r.returncode)
    return r

MSG=("rank 156: fold bench155-run359 (14hr band-first cold 7/60 ~11.7% heavy 6/20) + "
"bench156-run360 (1/60) -> K-Z3 14hr(9/7) 8/120 ~6.7% 2-set mid-high band; heavy single-window "
"non-sustained (run360 1/60, 9-min decay after run359A 6/20); rank/status/evolve unchanged "
"(K-Q1>K-Z2>K-Z3>K-S1>K-S2); NEXT K-Z3 14hr n-add run361")

# fetch latest first (non-fatal)
run(['git','fetch','bench_fetch'],check=False)
run(['git','rev-parse','HEAD'])
run(['git','rev-parse','bench_fetch/main'])
try:
    run(['git','status','--porcelain'])
except SystemExit:
    pass

# stage ONLY the state file (never the scratch .bXXX files)
r=run(['git','add','--','query-cosientist.md'])
r=run(['git','commit','-m',MSG],check=False)
LOG.append("COMMIT_RC=%d"%r.returncode)
run(['git','rev-parse','HEAD'])
# push detached HEAD to remote main via bench_fetch (fast-forward expected)
r=run(['git','push','bench_fetch','HEAD:main'],check=False)
LOG.append("PUSH_RC=%d"%r.returncode)
LOG.append("STDERR_TAIL: "+ (r.stderr[-400:] if r.stderr else "(none)"))

with open('/tmp/r156_commit_out.txt','w') as f:
    f.write("\n".join(LOG)+"\n")
print("done rc", r.returncode)
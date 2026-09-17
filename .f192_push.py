#!/usr/bin/env python3
import subprocess as sp
cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r=sp.run(["git","-C",cwd,"log","-1","--format=%H %ad %s"],capture_output=True,text=True)
print(r.stdout.strip())
p=sp.run(["git","-C",cwd,"push","net-kotobase","HEAD:main"],capture_output=True,text=True)
print("PUSH_RC="+str(p.returncode))
print(p.stdout.strip())
print(p.stderr.strip()[:2000])
#!/usr/bin/env python3
import subprocess as sp
import io
cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# fetch
r=sp.run(["git","-C",cwd,"fetch","net-kotobase"],capture_output=True,text=True)
head=sp.run(["git","-C",cwd,"rev-parse","HEAD"],capture_output=True,text=True).stdout.strip()
rm=sp.run(["git","-C",cwd,"rev-parse","net-kotobase/main"],capture_output=True,text=True).stdout.strip()
print("fetch_rc="+str(r.returncode))
print("HEAD="+head)
print("REMOTE="+rm)
print("MATCH="+str(head==rm))
# confirms us clean
if head!=rm:
    print("STALE-need-rebase")
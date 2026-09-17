#!/usr/bin/env python3
import subprocess
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
head=subprocess.run(["git","show","HEAD:query-cosientist.md"],capture_output=True).stdout.decode()
print("HEAD has 第161回:", head.count("第161回"))
print("HEAD has run347 in L279-style:", head.count("run347"))
print("HEAD has run348:", head.count("run348"))
wt=open(p,encoding="utf-8").read()
print("WORKTREE has 第161回:", wt.count("第161回"))
print("WORKTREE has run347:", wt.count("run347"))
print("WORKTREE has run348:", wt.count("run348"))
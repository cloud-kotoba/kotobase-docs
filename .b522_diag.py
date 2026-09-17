#!/usr/bin/env python3
import subprocess
def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    return r.stdout.strip()
print('--- log -4 ---')
print(sh('git log --oneline -4'))
print('--- who is ababb14 ---')
print(sh('git log -1 --format=%s ababb14'))
print('--- is ababb14 descendant of 7c24933? ---')
print(sh("git merge-base --is-ancestor 7c24933 ababb14 && echo YES || echo NO"))
print('--- ababb14 diff vs 7c24933 (doc) ---')
print(sh('git diff --stat 7c24933 ababb14 -- query-cosientist.md'))
#!/usr/bin/env python3
# run545 evidence append: K-Z3 row lacks trailing ' |'; append at end of line 279 (idx 278)
import io
DIR="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
fn=f"{DIR}/query-cosientist.md"
lines=io.open(fn,encoding="utf-8").read().split("\n")
kz3=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        kz3=i; break
assert kz3 is not None
row=lines[kz3]
ev=" falsify 第242回 run545 (9/9 10:30 JST, 10hr帯初計測): n=60 全200, cold>=0.5s 6/60 (~10.0%) (A3+B2+C1, max 1.5669s), control landing 0/20 完全静穏分離成立. load1 ~99."
assert "run545" not in row, "already appended"
newrow=row+ev
if not newrow.endswith("|"): newrow=newrow+" |"
lines[kz3]=newrow
# iter log insert
ilog=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        ilog=i; break
assert ilog is not None
ins=ilog+1
if lines[ins].strip()=="": ins+=1
iter_entry="- 2026-09-09: falsify 第242回: K-Z3 10時台帯初計測 run545 n積み増し cold 6/60 (~10.0%) (A3+B2+C1), control 0/20 完全静穏分離成立, iter/evidence 追記"
lines.insert(ins, iter_entry)
new="\n".join(lines)
comb=[c for c in set(new) if 0x0300<=ord(c)<=0x036F]
if comb:
    print("WARNING combining:",[hex(ord(c)) for c in comb])
    for c in comb: new=new.replace(c,"")
io.open(fn,"w",encoding="utf-8").write(new)
chk=io.open(fn,encoding="utf-8").read()
print("ev_count:",chk.count("falsify 第242回 run545"))
print("iter_count:",chk.count("falsify 第242回: K-Z3 10時台"))
print("new_tail:",repr(lines[kz3][-60:]))

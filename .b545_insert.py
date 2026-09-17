#!/usr/bin/env python3
# run545 evidence append to K-Z3 row end + iter log insert at top
import io, re, unicodedata, sys
DIR="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
fn=f"{DIR}/query-cosientist.md"
txt=io.open(fn,encoding="utf-8").read()
lines=txt.split("\n")
kz3_idx=None
ilog_idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |") and kz3_idx is None:
        kz3_idx=i
    if l.strip()=="## Iteration log" and ilog_idx is None:
        ilog_idx=i
assert kz3_idx is not None, "K-Z3 row not found"
assert ilog_idx is not None, "Iteration log header not found"
print(f"kz3_idx={kz3_idx} ilog_idx={ilog_idx}")
ev=" falsify 第242回 run545 (9/9 10:30 JST, 10hr帯初計測): n=60 全200, cold>=0.5s 6/60 (~10.0%) (A3+B2+C1, max 1.5669s), control landing 0/20 完全静穏分離成立. load1 ~99."
row=lines[kz3_idx]
assert row.rstrip().endswith("|"), "row must end with |"
lines[kz3_idx]=row.rstrip()[:-1].rstrip()+ev+" |"
iter_entry="- 2026-09-09: falsify 第242回: K-Z3 10時台帯初計測 run545 n積み増し cold 6/60 (~10.0%) (A3+B2+C1), control 0/20 完全静穏分離成立, iter/evidence 追記\n"
# insert after header line +following blank line if present
ins=ilog_idx+1
if lines[ins].strip()=="":
    ins+=1
lines.insert(ins, iter_entry.rstrip("\n"))
new="\n".join(lines)
# strip combining chars range just in case
comb=[(hex(ord(c)),c) for c in set(new) if 0x0300<=ord(c)<=0x036F]
if comb:
    print("WARNING combining:",comb)
    for _,c in comb: new=new.replace(c,"")
io.open(fn,"w",encoding="utf-8").write(new)
print("written")
# verify
chk=io.open(fn,encoding="utf-8").read()
print("ev_count:", chk.count("falsify 第242回 run545"))
print("iter_count:", chk.count("falsify 第242回: K-Z3 10時台"))

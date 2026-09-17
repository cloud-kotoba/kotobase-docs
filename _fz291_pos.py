import re
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_fz291_out.txt"
cur=None
rows={}
for line in open(p):
    line=line.rstrip("\n")
    if line.startswith("=== run"):
        cur=line.split()[1]; rows[cur]=[]
    elif line.startswith("=== landing"):
        cur="control"; rows[cur]=[]
    elif re.match(r"^\d{3} ",line):
        code,t=line.split(); rows[cur].append((len(rows[cur])+1,float(t)))
for k,v in rows.items():
    cold=[(i,t) for i,t in v if t>=0.5]
    print(f"{k}: cold_positions={cold}")
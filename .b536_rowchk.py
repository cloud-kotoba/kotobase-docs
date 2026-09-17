import sys
path='/tmp/bc_qc_head.md'
lines=open(path,encoding='utf-8').readlines()
row=lines[278]  # L279 index 278
with open('/tmp/bc_rowtail.txt','w',encoding='utf-8') as f:
    f.write("TOTAL_LINES %d\n"%len(lines))
    f.write("L279_LEN %d\n"%len(row))
    f.write("RUN535_IN_ROW %s\n"%('run535' in row))
    f.write("ROW_LAST_80_REPR: %r\n"%row[-80:])
    f.write("\n---ROW TAIL 1800 chars text---\n")
    f.write(row[-1800:])
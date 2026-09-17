import sys
files={'.b432_run432_A.txt':'run432A','.b432_run432_B.txt':'run432B','.b432_run432_C.txt':'run432C','.b432_run432_land.txt':'land'}
for f,lab in files.items():
    vals=[]; cold=0; http=0
    for line in open(f):
        p=line.split()
        if len(p)<3: continue
        try: t=float(p[1])
        except: continue
        vals.append(t)
        if t>=0.5: cold+=1
        if p[0]=='200': http+=1
    vals=sorted(vals)
    n=len(vals)
    p50=(vals[n//2]+vals[(n-1)//2])/2.0 if n else 0.0
    print(lab,'n',n,'200',http,'p50_ms',round(p50*1000,1),'max_s',round(vals[-1],4) if n else '-','cold',cold)
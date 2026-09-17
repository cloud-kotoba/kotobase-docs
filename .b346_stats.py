import sys, statistics
def load(path):
    toks=[]
    for line in open(path):
        p=line.split()
        if len(p)>=2:
            toks.append((p[0], float(p[1])))
    return toks
def nearest_rank_p50(vals):
    v=sorted(vals)
    n=len(v)
    r=(n*50 + 99)//100  # nearest-rank, 1-indexed ceiling
    if r<1: r=1
    if r>n: r=n
    return v[r-1]
def summarize(path, label):
    toks=load(path)
    codes=[c for c,t in toks]
    tt=[t for c,t in toks]
    cold=[t for c,t in toks if c=='200' and t>=0.5]
    n=len(tt)
    print(f"{label}: n={n} all200={all(c=='200' for c in codes)} cold={len(cold)}/{n} "
          f"p50={nearest_rank_p50(tt):.4f}s max={max(tt):.4f}s")
    if cold:
        print(f"  cold vals: "+", ".join(f"{t:.4f}" for t in sorted(cold)))
for name,label in [('.b346_346A.txt','run346A'),('.b346_346B.txt','run346B'),
                  ('.b346_346C.txt','run346C'),('.b346_land.txt','control(signup)')]:
    summarize(name,label)
print("=== time ===")
print(open('.b346_time.txt').read())
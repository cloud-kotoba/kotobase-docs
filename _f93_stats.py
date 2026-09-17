import statistics
fn = "_f93_run221_out.txt"
runs = {"run221A":[], "run221B":[], "run221C":[], "control":[]}
for line in open(fn):
    parts = line.split()
    if len(parts) < 2 or not parts[1].isdigit():
        continue
    tag, code, t = parts[0], int(parts[1]), float(parts[2])
    if tag in runs:
        runs[tag].append(t)
def p50(xs):
    return statistics.median(xs)
for tag in ["run221A","run221B","run221C","control"]:
    xs = runs[tag]
    cold = [x for x in xs if x >= 0.5]
    print(f"{tag}: n={len(xs)} cold={len(cold)}/20 p50={p50(xs)*1000:.1f}ms max={max(xs)*1000:.1f}ms cold_list={[round(x,3) for x in cold]}")
allsearch = runs["run221A"]+runs["run221B"]+runs["run221C"]
print(f"search total: cold={len([x for x in allsearch if x>=0.5])}/60 p50={p50(allsearch)*1000:.1f}ms")
ctl = runs["control"]
print(f"control: cold={len([x for x in ctl if x>=0.5])}/20 p50={p50(ctl)*1000:.1f}ms max={max(ctl)*1000:.1f}ms")
# per-position breakdown for A to detect clustering type
for tag in ["run221A","run221B","run221C"]:
    coldpos = [i+1 for i,x in enumerate(runs[tag]) if x >= 0.5]
    if coldpos:
        print(f"{tag} cold positions: {coldpos}")
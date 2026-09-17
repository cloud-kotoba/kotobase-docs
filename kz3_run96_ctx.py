import sys
hits = []
with open('query-cosientist.md') as f:
    for i, line in enumerate(f, 1):
        if 'run96' in line:
            # show context around each occurrence
            idx = 0
            while True:
                idx = line.find('run96', idx)
                if idx < 0: break
                hits.append(f"L{i}: ..." + line[max(0,idx-120):idx+260] + "...")
                idx += 5
sys.stdout.write(f"total hits: {len(hits)}\n")
for h in hits:
    sys.stdout.write(h + "\n---\n")

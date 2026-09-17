rows = []
with open('/tmp/.b583_re.tsv') as f:
    for line in f:
        p = line.split()
        if len(p) >= 3:
            rows.append((p[0], p[1], p[2]))
print(rows)

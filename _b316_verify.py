import io
with open('query-cosientist.md','r',encoding='utf-8') as f:
    lines=f.readlines()
print("=== ITER HEAD (line 359) ===")
print(lines[358][:300])
print("=== KZ3 line tail ===")
# find K-Z3 row line
kz3_idx=None
for i,l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        kz3_idx=i; break
print("kz3_idx(line no):", kz3_idx+1)
print(lines[kz3_idx][-450:])
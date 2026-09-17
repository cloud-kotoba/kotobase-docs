with open('_b82_evidence.txt', encoding='utf-8') as f:
    s = f.read()
s = s.replace('cold(>=0.9s)', 'cold(>=0.5s)')
with open('_b82_evidence.txt', 'w', encoding='utf-8') as f:
    f.write(s)
print('ok', s.count('cold(>=0.5s)'))

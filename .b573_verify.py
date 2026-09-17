import re

# Full audit of .b573_A.ttfb.bak: every raw line, classified, to determine
# the true sample count and whether the "other" non-200 codes were real
# curl write-errors (code 000) or parse artifacts of the token stream.

CODE_RE = re.compile(r"^\d{3}$")
FLOAT_RE = re.compile(r"^\d+\.\d+$")

with open(".b573_A.ttfb", encoding="utf-8") as f:
    raw = f.read()

lines = [l.strip() for l in raw.split("\n") if l.strip()]
print("raw lines:", len(lines))
for idx, line in enumerate(lines):
    parts = line.split()
    tag = []
    for p in parts:
        if CODE_RE.match(p):
            tag.append("CODE" + p)
        elif FLOAT_RE.match(p):
            tag.append("F")
        else:
            tag.append("?")
    print(idx, "|", line, "|", ",".join(tag))

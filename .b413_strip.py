#!/usr/bin/env python3
p = "docs/.b413_ins.py"
with open(p, "rb") as f:
    b = f.read()
# strip UTF-8 zero-width space (E2 80 8B) and other zero-width chars
for seq in [b"\xe2\x80\x8b", b"\xe2\x80\x8c", b"\xe2\x80\x8d", b"\xe2\x80\x8e", b"\xe2\x80\x8f", b"\xe2\x80\xaa", b"\xe2\x80\xab", b"\xe2\x81\xa0", b"\xe2\x81\xa1", b"\xe2\x81\xa2", b"\xe2\x81\xa3"]:
    b = b.replace(seq, b"")
with open(p, "wb") as f:
    f.write(b)
print("stripped; now", len(b), "bytes")